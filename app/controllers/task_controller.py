import uuid
from datetime import datetime, timezone

from dynamodb_manager import DynamoDBManager
from models.task import Task


class TaskController:
    def __init__(self):
        self.dynamodb_manager = DynamoDBManager(
            region_name='us-east-2', table_name='TasksTable')

    def create_task(self, data):
        try:
            code = str(uuid.uuid4())
            current_datetime = datetime.now(timezone.utc).isoformat()
            task = Task(code, data['description'], data['status'],
                        current_datetime, current_datetime)
            self.dynamodb_manager.put_item(task.to_dynamo())
            return code
        except Exception as e:
            raise Exception('Failed to create task') from e

    def _remove_dynamo_attributes(self, task):
        return {k: v['S'] if isinstance(v, dict) and 'S' in v else v for k,
                v in task.items()}

    def get_tasks(self):
        try:
            tasks = self.dynamodb_manager.scan_items()
            formatted_tasks = [
                Task(**self._remove_dynamo_attributes(task))
                .to_dict() for task in tasks]
            return formatted_tasks
        except Exception as e:
            raise Exception('Failed to get tasks') from e

    def get_task(self, code):
        try:
            task = self.dynamodb_manager.get_item({'code': {'S': code}})
            if task:
                return Task(**self._remove_dynamo_attributes(task)).to_dict()
            else:
                raise Exception('Task not found')
        except Exception as e:
            raise Exception('Failed to get task') from e

    def update_task(self, code, data):
        try:
            task = self.get_task(data['code'])
            current_datetime = datetime.now(timezone.utc).isoformat()
            task = Task(code, task.description, data['status'],
                        task.created_at, current_datetime)
            self.dynamodb_manager.put_item(task.to_dynamo())
        except Exception as e:
            raise Exception('Failed to update task') from e

    def delete_task(self, code):
        try:
            self.dynamodb_manager.delete_item({'code': {'S': code}})
        except Exception as e:
            raise Exception('Failed to delete task') from e
