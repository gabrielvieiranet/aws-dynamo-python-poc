class Task:
    def __init__(self, code, description, status, created_at, updated_at):
        self.code = code
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            'code': self.code,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def to_dynamo(self):
        return {
            'code': {'S': self.code},
            'description': {'S': self.description},
            'status': {'S': self.status},
            'created_at': {'S': self.created_at},
            'updated_at': {'S': self.updated_at}
        }
