#!/usr/bin/python3
"""
Queries the Reddit API to get the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
            Returns the number of subscribers for a given subreddit.

                Args:
                        subreddit (str): The name of the subreddit.

                            Returns:
                                    int: The number of subscribers, or 0 if the subreddit is invalid.
                                        """
                                            url = f'https://www.reddit.com/r/{subreddit}/about.json'
                                                headers = {'User-Agent': 'MyBot/0.1'}  # Set a custom User-Agent to avoid Too Many Requests error

                                                    response = requests.get(url, headers=headers)

                                                        if response.status_code == 200:
                                                            data = response.json()
                                                                            subscribers = data['data']['subscribers']
                                                                                    return subscribers
                                                                                else:
                                                                                    return 0

                                                                                if __name__ == '__main__':
                                                                                    import sys

                                                                                                        if len(sys.argv) < 2:
                                                                                                            print("Please pass an argument for the subreddit to search.")
                                                                                                        else:
                                                                                                            subreddit = sys.argv[1]
                                                                                                                                            num_subscribers = number_of_subscribers(subreddit)
                                                                                                                                                    print(num_subscribers)
