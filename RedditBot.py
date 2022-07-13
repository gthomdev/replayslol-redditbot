import praw
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

import RedditBotHelpers


def main():
    load_dotenv()

    target_subreddit = 'SummonerSchool'
    target_submission_count = 4000
    reddit = praw.Reddit(
        user_agent="testbot",
        client_id=os.environ.get('REDDIT_CLIENT_ID'),
        client_secret=os.environ.get('REDDIT_CLIENT_SECRET'),
        username=os.environ.get('REDDIT_USERNAME'),
        password=os.environ.get('REDDIT_PASSWORD')
    )
    with open("Comments.txt", 'w', encoding="utf-8") as infile:
        for submission in reddit.subreddit(target_subreddit).new(limit=target_submission_count):
            if hasattr(submission, "selftext_html"):
                soup = BeautifulSoup(submission.selftext_html, 'html.parser')
                for link in soup.findAll('a', href=True):
                    if RedditBotHelpers.is_target_link_type(link.attrs['href']):
                        infile.write(link.attrs['href'] + "\n")

if __name__ == "__main__":
    main()

