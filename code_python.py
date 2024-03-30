from getpass import getpass
import json
import logging
from datetime import datetime, timedelta, timezone

import boto3
import pyarrow as pa
import pyarrow.parquet as pq
import requests

# Autentica o token
token = getpass()

# Conecta com a API por meio do token
base_url = f'https://api.telegram.org/bot{token}'

# Retorna informações sobre o bot.
response = requests.get(url=f'{base_url}/getMe')
print(json.dumps(json.loads(response.text), indent=2))

# Instala a biblioteca boto3
!pip install boto3
import boto3

def lambda_handler(event: dict, context: dict) -> dict:
    '''
    Recebe uma mensagem do Telegram via AWS API Gateway, verifica se foi produzida em um determinado grupo
    e a escreve, em seu formato original JSON, em um bucket do AWS S3.
    '''
    # vars de ambiente
    BUCKET = os.environ['AWS_S3_BUCKET']
    TELEGRAM_CHAT_ID = int(os.environ['TELEGRAM_CHAT_ID'])
    # vars lógicas
    tzinfo = timezone(offset=timedelta(hours=-3))
    date = datetime.now(tzinfo).strftime('%Y-%m-%d')
    timestamp = datetime.now(tzinfo).strftime('%Y%m%d%H%M%S%f')
    filename = f'{timestamp}.json'
    # código principal
    client = boto3.client('s3')
    try:
        message = json.loads(event["body"])
        chat_id = message["message"]["chat"]["id"]
        if chat_id == TELEGRAM_CHAT_ID:
            with open(f"/tmp/{filename}", mode='w', encoding='utf8') as fp:
                json.dump(message, fp)
            client.upload_file(f'/tmp/{filename}', BUCKET, f'telegram/context_date={date}/{filename}')
    except Exception as exc:
        logging.error(msg=exc)
        return dict(statusCode="500")
    else:
        return dict(statusCode="200")

# Configuração da URL do AWS API Gateway
aws_api_gateway_url = getpass()
response = requests.get(url=f'{base_url}/setWebhook?url={aws_api_gateway_url}')
print(json.dumps(json.loads(response.text), indent=2))
response = requests.get(url=f'{base_url}/getWebhookInfo')
print(json.dumps(json.loads(response.text), indent=2))

# ETL

def lambda_handler(event: dict, context: dict) -> bool:
    '''
    Diariamente é executado para compactar as diversas mensagensm, no formato JSON, do dia anterior,
    armazenadas no bucket de dados cru, em um único arquivo no formato PARQUET, armazenando-o no bucket
    de dados enriquecidos
    '''
    # vars de ambiente
    BUCKET = os.environ['AWS_S3_BUCKET']
    TELEGRAM_CHAT_ID = int(os.environ['TELEGRAM_CHAT_ID'])
    # vars lógicas
    tzinfo = timezone(offset=timedelta(hours=-3))
    date = (datetime.now(tzinfo) - timedelta(days=1)).strftime('%Y-%m-%d')
    timestamp = datetime.now(tzinfo).strftime('%Y%m%d%H%M%S%f')
    # código principal
    table = None
    client = boto3.client('s3')
    try:
        response = client.list_objects_v2(Bucket=RAW_BUCKET, Prefix=f'telegram/context_date={date}')
        for content in response['Contents']:
            key = content['Key']
            client.download_file(RAW_BUCKET, key, f"/tmp/{key.split('/')[-1]}")
            with open(f"/tmp/{key.split('/')[-1]}", mode='r', encoding='utf8') as fp:
                data = json.load(fp)
                data = data["message"]
            parsed_data = parse_data(data=data)
            iter_table = pa.Table.from_pydict(mapping=parsed_data)
            if table:
                table = pa.concat_tables([table, iter_table])
            else:
                table = iter_table
                iter_table = None
        pq.write_table(table=table, where=f'/tmp/{timestamp}.parquet')
        client.upload_file(f"/tmp/{timestamp}.parquet", ENRICHED_BUCKET, f"telegram/context_date={date}/{timestamp}.parquet")
        return True
    except Exception as exc:
        logging.error(msg=exc)
        return False

# Data Wrangling

def parse_data(data: dict) -> dict:
    date = datetime.now().strftime('%Y-%m-%d')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    parsed_data = dict()
    for key, value in data.items():
        if key == 'from':
            for k, v in data[key].items():
                if k in ['id', 'is_bot', 'first_name']:
                    parsed_data[f"{key if key == 'chat' else 'user'}_{k}"] = [v]
        elif key == 'chat':
            for k, v in data[key].items():
                if k in ['id', 'type']:
                    parsed_data[f"{key if key == 'chat' else 'user'}_{k}"] = [v]
        elif key in ['message_id', 'date', 'text']:
            parsed_data[key] = [value]
    if 'text' not in parsed_data.keys():
        parsed_data['text'] = [None]
    return parsed_data
