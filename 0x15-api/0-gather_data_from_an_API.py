#!/usr/bin/python3
"""script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests as req
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = int(sys.argv[1])
    usr_id = req.get(url + 'users/{}'.format(emp_id)).json()
    to_do = req.get(url + 'todos', params={'userId': emp_id}).json()

    completed = []
    for title in to_do:
        if title.get("completed", False):
            completed.append(title["title"])
    print(completed)
    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),
                                                          len(completed),
                                                          len(to_do)))
    [print(f"\t {title}") for title in completed]
