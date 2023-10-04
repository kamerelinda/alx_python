#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her tasks,  extend your Python script to export data in the CSV format. """


import requests
import sys
import csv

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

        # Create a CSV file for the employee
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write tasks to the CSV file
            for task in todo_data:
                task_completed_status = "True" if task['completed'] else "False"
                task_title = task['title']
                csv_writer.writerow([employee_id, employee_name, task_completed_status, task_title])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print(f"Error: Employee with ID {employee_id} not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    main()
