provider "aws" {
  region = "us-east-2"
}

resource "aws_dynamodb_table" "tasks_table" {
  name         = "TasksTable"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "code"

  attribute {
    name = "code"
    type = "S"
  }
}
