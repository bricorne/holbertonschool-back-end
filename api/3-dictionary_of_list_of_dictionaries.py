#!/usr/bin/python3
'''Python script that returns information using REST API'''

import json
import requests
import sys


def get_employee_todo_progress():
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users_data = requests.get(users_url).json()
    todos_data = requests.get(todos_url).json()

    all_tasks = {}

    for user in users_data:
        user_id = str(user["id"])
        all_tasks[user_id] = []

        for task in todos_data:
            if task["userId"] == user["id"]:
                task_dict = {}
                task_dict["username"] = user["username"]
                task_dict["task"] = task["title"]
                task_dict["completed"] = task["completed"]
                all_tasks[user_id].append(task_dict)

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)

if __name__ == "__main__":
    get_employee_todo_progress()
