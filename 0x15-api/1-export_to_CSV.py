#!/usr/bin/python3
"""script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
export the data into csv file
"""
import csv
import requests as req
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr_id = int(sys.argv[1])
    usr = req.get(url + 'users/{}'.format(usr_id)).json()
    username = usr.get("username")
    to_do = req.get(url + 'todos', params={'userId': usr_id}).json()

    completed = []
    for title in to_do:
        if title.get("completed", False):
            completed.append(title["title"])
    print("Employee {} is done with tasks({}/{}):".format(usr.get("name"),
                                                          len(completed),
                                                          len(to_do)))
    [print(f"\t {title}") for title in completed]
    # open write the data into a csv file using the user id
    with open(f"{usr_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # make a list of the userId, the username, the completed
        # task status and thetitle
        writer.writerows([usr_id, username, task.get("completed"),
                          task.get("title")] for task in to_do)
