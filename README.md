# Pipeline de Dados do Telegram

Projeto: Integração Telegram com AWS S3

## Funcionalidades:
Receber Mensagens do Telegram via AWS API Gateway:

O projeto recebe mensagens do Telegram por meio da AWS API Gateway.
Verifica se as mensagens foram produzidas em um determinado grupo.
Armazenamento no AWS S3:

As mensagens, em seu formato original JSON, são escritas em um bucket do AWS S3.
As mensagens são organizadas em subdiretórios com base na data de recebimento.
Compactação e Armazenamento em Formato Parquet:

Diariamente, as mensagens do dia anterior são compactadas em um único arquivo no formato Parquet.
O arquivo compactado é armazenado em um bucket separado do AWS S3 para dados enriquecidos.

## Como Usar:

Configuração do Token do Telegram:

Execute o código Python fornecido.
Você será solicitado a inserir o token do seu bot do Telegram.
Conectar com a API do Telegram:

O código conecta-se à API do Telegram para obter informações sobre o bot e configurar o webhook.
Configuração das Variáveis de Ambiente:

Defina as variáveis de ambiente AWS_S3_BUCKET e TELEGRAM_CHAT_ID para especificar o bucket do AWS S3 e o ID do chat do Telegram, respectivamente.
Execução do Lambda Handler:

O lambda_handler recebe as mensagens do Telegram, verifica se foram produzidas no chat especificado e as armazena no AWS S3.
Execução do ETL:

Através do lambda_handler temos a exeção uma etapa de ETL diária.
Compacta as mensagens JSON do dia anterior em um único arquivo Parquet e armazena-o em um bucket separado.
Data Wrangling:

O código realiza uma etapa de Data Wrangling nas mensagens antes de compactá-las em Parquet.
Ele extrai informações relevantes das mensagens JSON do Telegram.

## Observações

Certifique-se de ter instalado o Python e as bibliotecas necessárias, incluindo boto3, requests e pyarrow.
É necessário ter uma conta na AWS com permissões para criar e gerenciar serviços como S3 e Lambda.
Configurações AWS:

Antes de usar o código, configure as credenciais da AWS no ambiente de execução.
Certifique-se de que as permissões necessárias estejam configuradas para acessar os serviços da AWS.

Manutenção:

Este projeto pode ser adaptado para atender a diferentes requisitos ou integrado a outros sistemas.
Mantenha as variáveis de ambiente e as configurações do AWS atualizadas conforme necessário.

Segurança:

Certifique-se de que todas as informações confidenciais, como tokens de acesso e chaves de API, sejam armazenadas de forma segura e não expostas no código fonte ou em repositórios públicos.
Para criar e gerenciar serviços como S3 e Lambda, é necessário ter uma conta AWS com permissões apropriadas. Aqui estão as configurações da AWS necessárias:

Para utilizar o código, é necessário configurar suas credenciais AWS no ambiente de execução. É fundamental configurar corretamente as permissões necessárias para acessar seus serviços AWS.

Manutenção:

Você tem a flexibilidade de personalizar este projeto para atender a diversas necessidades ou incorporá-lo perfeitamente em sistemas existentes. Lembre-se de atualizar regularmente as variáveis ​​e configurações de ambiente da AWS para garantir que tudo permaneça atualizado.

Segurança:

É crucial armazenar com segurança e evitar a exposição de informações confidenciais, como tokens de acesso e chaves de API, no código-fonte ou em repositórios públicos.


Project: Telegram integration with AWS S3

Features:
Receive Telegram messages via AWS API Gateway:

The project receives messages from Telegram via the AWS API Gateway. It checks whether messages have been produced in a particular group. Storage in AWS S3:

Messages, in their original JSON format, are written to an AWS S3 bucket. Messages are organized into subdirectories based on the date they were received. Compression and storage in parquet format:

Every day, the previous day's messages are compressed into a single file in Parquet format. The compressed file is stored in a separate AWS S3 bucket for enriched data.

How to use:
Telegram Token Configuration:

Run the Python code provided. You will be prompted to enter your Telegram bot token. Connect to the Telegram API:

The code connects to the Telegram API to get information about the bot and configure the webhook. Setting Environment Variables:

Set the AWS_S3_BUCKET and TELEGRAM_CHAT_ID environment variables to specify the AWS S3 bucket and Telegram chat ID, respectively. Execution of the Lambda Handler:

The lambda_handler receives the Telegram messages, checks whether they were produced in the specified chat and stores them in AWS S3. ETL execution:

Through the lambda_handler we have the exception of a daily ETL step. It compresses the previous day's JSON messages into a single Parquet file and stores it in a separate bucket. 

Data Wrangling:
The code performs a Data Wrangling step on the messages before compressing them into Parquet.
It extracts relevant information from Telegram JSON messages.

## Notes

Make sure you have Python and the necessary libraries installed, including boto3, requests and pyarrow.
You must have an AWS account with permissions to create and manage services such as S3 and Lambda.
AWS configurations:

Before using the code, set up the AWS credentials in the execution environment.
Make sure that the necessary permissions are configured to access AWS services.
Maintenance:

This project can be adapted to meet different requirements or integrated with other systems.
Keep the environment variables and AWS settings updated as necessary.
Security:

Make sure that all sensitive information, such as access tokens and API keys, is stored securely and not exposed in the source code or in public repositories.
To create and manage services like S3 and Lambda, you need an AWS account with appropriate permissions. Here are the AWS settings required:

To use the code, you need to configure your AWS credentials in the runtime environment. It is essential to correctly configure the permissions required to access your AWS services.

Maintenance:

You have the flexibility to customize this project to suit different needs or incorporate it seamlessly into existing systems. Remember to regularly update your AWS environment variables and settings to make sure everything stays up to date.

Security:

It is crucial to store securely and avoid exposing sensitive information, such as access tokens and API keys, in the source code or in public repositories.





