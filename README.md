# AWS - POC PYTHON + DYNAMODB

Teste de conexão de API com DynamoDB.

Dentro de infra tem uma config para criar uma tabela simples no DynamoDB utilizando Terraform

Dentro de app fica um código em Python de um serverzinho em Flask para interagir com essa tabela

## Crie uma configuração para acesso ao ambiente de sua conta AWS

Precisamos de uma credencial para que nosso código se conecte no ambiente AWS.

Como pré requisito, já é esperado que você tenha uma conta AWS Free Tier configurada.

Depois disso, logue na sua conta AWS e lá em IAM / Users, crie um usuário com perfil ADMIN.
Depois, dentro das configs desse usuário, vá na aba Security credentials e crie uma Access Key.
Essa Access Key será utilizada em nossa aplicação, só que ela ficará configurada no ambiente, fora do código.
Ela possui dois valores. Guarde bem esses valores e não compartilhe.

Agora para configurar a Access Key no ambiente, crie o diretório ~/.aws com dois arquivos (segue meu exemplo):

**~/.aws/config**
```
[default]
region = us-east-2
output = json
```

**~/.aws/credentials**
```
[default]
aws_access_key_id=********************
aws_secret_access_key=****************************************
```

Este segundo arquivo `credentials` vai conter a Access Key que você criou. É só substituir ali no lugar dos asteriscos.

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
Acesse o webserver Flask no navegador em `http://127.0.0.1:5000`