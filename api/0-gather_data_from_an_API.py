#!/usr/bin/python3
"""for a given employee ID, returns information about his TODO list progress"""
import sys
import requests


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)

        if employee_response.status_code == 200 and todos_response.status_code == 200:
            employee_data = employee_response.json()
            todos_data = todos_response.json()

            employee_name = employee_data["name"]
            total_tasks = len(todos_data)
            done_tasks = sum(1 for task in todos_data if task["completed"])
            completed_task_titles = [task["title"] for task in todos_data if task["completed"]]

            print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
            for title in completed_task_titles:
                print(f"     {title}")

        else:
            print("Failed to retrieve data from the API.")

    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
