# py program to export data in csv format

import csv
import requests
import sys

def get_employee_info(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if not employee_data:
        print(f"Error: Employee with ID {employee_id} not found.")
        return
    
    employee_name = employee_data['name']
    user_id = employee_data['id']

    # fetching the TODO list for the employee
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # calculating the TODO list progress
    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)

    # to output employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    # to output titles of completed taskes
    for task in todo_data:
        if task['completed']:
            print(f"\t {task['title']}")

     
    # to output TODO llist data to csv
    csv_filename = f'{user_id}.csv'
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()
        for task in todo_data:
            csv_writer.writerow({
                "USER_ID": user_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(task['completed']),
                "TASK_TITLE": task['title']
            })

    print(f"TODO list data exported to {csv_filename}")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
    