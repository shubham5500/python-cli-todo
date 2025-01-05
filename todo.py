import sys
import json
from datetime import datetime

DATA_FILE = './todo.json'

STATUS_ENUMS = {
    'TODO': 'todo',
    'IN_PROGRESS': 'in-progress',
    'DONE': 'done'
}


def load_tasks():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_todos(todos):
    with open(DATA_FILE, 'w') as file:
        json.dump(todos, file, indent=1)


def add_todo(task):
    tasks = load_tasks()
    tasks.append(task)
    save_todos(tasks)


args = sys.argv

type = args[1]

if (type == 'add'):
    tasks = load_tasks()
    id = tasks[len(tasks) - 1]['id'] + 1 if tasks else 0
    task = {
        'id': id,
        'desc': args[2],
        'created_at': str(datetime.now()),
        'updated_at': str(datetime.now()),
        'status': STATUS_ENUMS['TODO']
    }
    # print(task)
    add_todo(task)
elif type == 'update':
    tasks = load_tasks()
    id = args[2]
    description = args[3]
    task = [t for t in tasks if t.id == id]
    task['desc'] = description

elif type == 'mark-in-progress':
    # print('aya')
    tasks = load_tasks()
    id = args[2]

    def mark_in_progress(task):
        print(task)
        if task['id'] == int(id):
            task['status'] = STATUS_ENUMS['IN_PROGRESS']
            return task
        return task

    updated_tasks = list(map(lambda task: mark_in_progress(task), tasks))
    save_todos(updated_tasks)

elif type == 'mark-done':
    # print('aya')
    tasks = load_tasks()
    id = args[2]

    def mark_done(task):
        print(task)
        if task['id'] == int(id):
            task['status'] = STATUS_ENUMS['DONE']
            return task
        return task

    updated_tasks = list(map(lambda task: mark_done(task), tasks))
    save_todos(updated_tasks)

elif type == 'delete':
    tasks = load_tasks()
    id = args[2]
    updated_tasks = list(filter(lambda task: task['id'] != int(id), tasks))
    save_todos(updated_tasks)

elif type == 'list':
    tasks = load_tasks()
    list_type = args[2] if len(args) > 2 else None
    print(list_type)
    if (list_type == 'done'):
        done_list = list(filter(lambda task: task['status'] == 'done', tasks))
        print(done_list)
    elif (list_type == 'in-progress'):
        in_progress_list = list(
            filter(lambda task: task['status'] == 'in-progress', tasks))
        print(in_progress_list)
    elif (list_type == 'todo'):
        todo_list = list(
            filter(lambda task: task['status'] == 'todo', tasks))
        print(todo_list)
    else:
        print(tasks)

