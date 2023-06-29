from controllers.task_controller import TaskController
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
task_controller = TaskController()


@app.errorhandler(Exception)
def handle_error(e):
    response = jsonify({'error': str(e)})
    response.status_code = 500
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = task_controller.get_tasks()
        return jsonify(tasks)
    except Exception as e:
        raise Exception('Failed to get tasks') from e


@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        code = task_controller.create_task(data)
        return jsonify({'code': code}), 201
    except Exception as e:
        raise Exception('Failed to create task') from e


@app.route('/tasks/<code>', methods=['GET'])
def get_task(code):
    try:
        task = task_controller.get_task(code)
        return jsonify(task)
    except Exception as e:
        raise Exception('Failed to get task') from e


@app.route('/tasks/<code>', methods=['PUT'])
def update_task(code):
    try:
        data = request.get_json()
        task_controller.update_task(code, data)
        return jsonify({'code': code})
    except Exception as e:
        raise Exception('Failed to update task') from e


@app.route('/tasks/<code>', methods=['DELETE'])
def delete_task(code):
    try:
        task_controller.delete_task(code)
        return jsonify({'message': 'Task deleted'})
    except Exception as e:
        raise Exception('Failed to delete task') from e


if __name__ == "__main__":
    app.run(debug=True)
