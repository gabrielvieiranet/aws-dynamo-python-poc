# AWS - POC PYTHON + DYNAMODB

Teste de conexão de API com DynamoDB.

## Crie uma configuração para acesso ao ambiente de sua conta AWS

Primeiro logue na sua conta AWS e lá em IAM / Users, crie um usuário com perfil ADMIN.
Depois, dentro das configs usuário, vá na aba Security credentials e crie uma Access Key.
Essa Access Key deve ter dois valores. Guarde bem esses valores e não compartilhe.

Depois crie o diretório ~/.aws com dois arquivos (segue meu exemplo):

~/.aws/config
```
[default]
region = us-east-2
output = json
```

~/.aws/credentials
```
[default]
aws_access_key_id=********************
aws_secret_access_key=****************************************
```

Este segundo arquivo `credentials` vai conter a Access Key que você criou.
Depois a lib boto3 do Python e o Terraform vão identificar sua credencial automaticamente.

Para criar a tabela no DynamoDB segue a lista de comandos Terraform:

```
cd infra
terraform init
terraform validate
terraform plan
terraform apply
```

Depois de criar a tabela no DynamoDB, baixe as libs em Python necessárias e inicie a aplicação localmente:

```
cd app
python -m pip install -Ur requirements.txt
python main.py
```
