#!/usr/bin/python3
"""a module that defines the top_ten function"""
import requests


def top_ten(subreddit):
    """Return the top ten reddits posts of a subreddit.

    arguments:
        subreddit -- the subreddit to be checked
    Return: the top ten reddits posts 
    """
    
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    useraAgent = requests.get('https://httpbin.org/user-agent').json()['user-agent']
    headers = {
        "User-Agent": useraAgent
    }
    params = {
        "limit": 10
    }
    res = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    results = res.json().get("data")
    [print(x.get("data").get('title')) for x in results.get("children")]
    