"""
    Created by Ma. Micah Encarnacion on 25/08/2020
"""
import requests
from bs4 import BeautifulSoup


def get_number_of_followers(username):
    if not isinstance(username, str):
        return TypeError("Username should be string!")

    temp = requests.get("https://mobile.twitter.com/" + username)

    bs = BeautifulSoup(temp.text, features="html.parser")

    try:
        profile_stats = bs.find("td", {"class": "stat-last"})
        followers = profile_stats.find("div", {"class": "statnum"})

        return followers.text
    except AttributeError:
        print("Account name not found...")


if __name__ == "__main__":
    account_handle = input(
        'Input Twitter username or follow this format ("https://twitter.com/<username>"): '
    )

    username = account_handle.split("/")[-1]

    number_of_followers = get_number_of_followers(username=username)
    print(f"{username} has {number_of_followers or 0} followers.")
