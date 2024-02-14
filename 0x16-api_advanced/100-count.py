#!/usr/bin/python3

"""
Module: subreddit_utils.py

This module contains functions related to querying the Reddit API recursively and counting words.
"""

import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): A token indicating the post to start after (default is None).
        word_count (Counter): A Counter object to store the word counts (default is None).

    Returns:
        None
    """
    if word_count is None:
        word_count = Counter()

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                for word in word_list:
                    if title.count(word.lower()) > 0:
                        word_count[word.lower()] += title.count(word.lower())
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    print("{}: {}".format(word, count))
    else:
        return


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2].split())
