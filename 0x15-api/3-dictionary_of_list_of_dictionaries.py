#!/usr/bin/python3
"""script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
export the data into csv file
"""
import json
import requests as req
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    # usr_id = int(sys.argv[1])
    usrs = req.get(url + 'users').json()
    to_dos = req.get(url + 'todos').json()
    # print(to_do)

    # # open write the data into a csv file using the user id
    with open("todo_all_employees.json", "w", newline="") as jsonfile:
        tasklist = []
        for usr in usrs:
            for task in to_dos:
                tasklist.append({usr.get("id"): [{
                    "username": usr.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }]})

        json.dump(list1, jsonfile)
