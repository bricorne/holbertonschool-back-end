#!/usr/bin/python3
'''
Python script that returns information using REST API
'''
import requests
import sys

if __name__ == "__main__":
    get_emp_id = sys.argv[1]
    user_url = (f'https://jsonplaceholder.typicode.com/users/{get_emp_id}')
    get_emp_data = requests.get(user_url).json()
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={get_emp_id}')
    get_emp_tasks = requests.get(todos_url).json()

    done_tasks = [task for task in get_emp_tasks if task.get("completed")]

    print(
        f"Employee {get_emp_data['name']} is done with "
        f"tasks({len(done_tasks)}/{len(get_emp_tasks)}):"
    )
    for task in done_tasks:
        print("\t", task["title"])