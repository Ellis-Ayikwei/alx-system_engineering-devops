#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    useraAgent = requests.get('https://httpbin.org/user-agent').json()
    useraAgent = useraAgent['user-agent']
    headers = {
        "User-Agent": useraAgent
    }

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            return 0

        results = res.json().get("data")
        return results.get("subscribers", 0)

    except requests.RequestException:
        return 0
    except ValueError:
        return 0
