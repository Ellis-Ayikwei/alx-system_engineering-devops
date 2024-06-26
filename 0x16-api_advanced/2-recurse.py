#!/usr/bin/python3
"""module that defines the recursive get of subreddits"""
import requests


def recurse(subreddit, hot_list=[],  after="", count=0):
    """function that queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    useraAgent = requests.get('https://httpbin.org/user-agent').json()
    useraAgent = useraAgent['user-agent']
    headers = {
        "User-Agent": useraAgent
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    res = requests.get(url,  headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print("None")
        return

    results = res.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
