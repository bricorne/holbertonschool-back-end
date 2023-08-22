#!/usr/bin/python3
'''Python script that returns information using REST API'''

import requests
import sys


def get_employee_todo_progress(emp_id):
    base_url = (f'https://jsonplaceholder.typicode.com/users/{emp_id}')
    emp_data = requests.get(base_url).json()
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}')

    total_tasks = requests.get(todos_url).json()

    done_tasks = [task for task in total_tasks if task.get("completed")]

    print(
        f"Employee {emp_data['name']} is done with "
        f"tasks({len(done_tasks)}/{len(total_tasks)}):"
    )
    for task in done_tasks:
        print("\t", task["title"])


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    get_employee_todo_progress(emp_id)