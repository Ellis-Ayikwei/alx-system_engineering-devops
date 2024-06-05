#!/usr/bin/python3
"""the count module"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    recursive function that queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords
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
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    try:
        results = res.json()
        if res.status_code != 200:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for child in results.get("children"):
        title = child.get("data").get("title").lower().split()
        for a_word in word_list:
            if a_word.lower() in title:
                times = title.count(a_word.lower())
                if instances.get(a_word) is None:
                    instances[a_word] = times
                else:
                    instances[a_word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print(f"{k}: {v}") for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
