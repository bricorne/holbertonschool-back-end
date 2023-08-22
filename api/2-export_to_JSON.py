#!/usr/bin/python3
'''Python script that returns information using REST API'''

import json
import requests
import sys


def get_employee_todo_progress(emp_id):
    base_url = (f'https://jsonplaceholder.typicode.com/users/{emp_id}')
    emp_data = requests.get(base_url).json()
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}')

    total_tasks = requests.get(todos_url).json()

    done_tasks = [task for task in total_tasks if task.get("completed")]

    tasks_list = []
    for task in total_tasks:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = emp_data.get("username")
        tasks_list.append(task_dict)

    tasks_json = {}
    tasks_json[emp_id] = tasks_list

    with open("{}.json".format(emp_id), 'w') as jsonfile:
        json.dump(tasks_json, jsonfile)