#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if invalid.
    """
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    useraAgent = requests.get('https://httpbin.org/user-agent').json()['user-agent']

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
