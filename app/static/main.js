document.addEventListener('DOMContentLoaded', function() {
    loadTasks();

    document.getElementById('task-form').addEventListener('submit', function(event) {
        event.preventDefault();
        createTask();
    });
});

function loadTasks() {
    fetch('/tasks')
        .then(response => response.json())
        .then(data => {
            const taskList = document.getElementById('task-list');
            taskList.innerHTML = '';

            data.forEach(task => {
                const taskItem = document.createElement('li');
                const taskDescription = document.createElement('span');

                taskDescription.textContent = task.description;

                taskItem.appendChild(taskDescription);

                taskList.appendChild(taskItem);
            });
        })
        .catch(error => console.log('Error:', error));
}

function createTask() {
    const description = document.getElementById('task-description').value;

    const taskData = {
        description: description,
        status: 'open'
    };

    fetch('/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(taskData)
    })
        .then(response => response.json())
        .then(data => {
            loadTasks();
        })
        .catch(error => console.log('Error:', error));
}
