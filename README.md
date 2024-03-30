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

O lambda_handler também executa uma etapa de ETL diária.
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
