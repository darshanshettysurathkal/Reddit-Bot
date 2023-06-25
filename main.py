import os.path
import time

import praw

import config


def reddit_login():
    print("logging in")
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="Pretty-Sector5195's dog comment responder v0.1")
    print("logged in")
    return r


def run_reddit(r, comments_replied_to):
    for comment in r.subreddit("test").comments(limit=25):
        if "dog" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print(f"comment found in {comment.id}")
            comment.reply(" i also love dogs ! [Here](https://imgur.com/gallery/A8eQsll) is a image of one")
            print(f"replied to comment {comment.id}")
            comments_replied_to.append(comment.id)

            with open("comments_replied_to", "a") as f:
                f.write(comment.id + "\n")

    time.sleep(10)


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
     with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read().split("\n")
    return comments_replied_to


r = reddit_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    run_reddit(r, comments_replied_to)

