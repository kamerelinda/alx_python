#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her tasks. """


import requests
import sys

employee_id = int(sys.argv[1])


def main():
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    try:
        # Fetch employee information
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data['name']

        # Fetch tasks list for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Calculate progress
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task['completed'])

        # Print employee tasks list progress
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

        # Print titles of completed tasks
        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print(f"Error: Employee with ID {employee_id} not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    main()
