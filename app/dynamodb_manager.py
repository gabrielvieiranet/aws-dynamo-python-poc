import boto3


class DynamoDBManager:
    def __init__(self, region_name, table_name):
        self.dynamodb = boto3.client('dynamodb', region_name=region_name)
        self.table_name = table_name

    def scan_items(self):
        response = self.dynamodb.scan(TableName=self.table_name)
        return response.get('Items', [])

    def get_item(self, key):
        response = self.dynamodb.get_item(TableName=self.table_name, Key=key)
        return response.get('Item')

    def put_item(self, item):
        self.dynamodb.put_item(TableName=self.table_name, Item=item)

    def delete_item(self, key):
        self.dynamodb.delete_item(TableName=self.table_name, Key=key)
