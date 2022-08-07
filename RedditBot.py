import praw
import os
import json
from time import sleep
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from Errors import SubmissionExistsException
import RedditBotHelpers
import Errors

def main():
    load_dotenv()

    target_subreddit = 'Summonerschool'
    target_submission_count = 4000
    reddit = praw.Reddit(
        user_agent="testbot",
        client_id=os.environ.get('REDDIT_CLIENT_ID'),
        client_secret=os.environ.get('REDDIT_CLIENT_SECRET'),
        username=os.environ.get('REDDIT_USERNAME'),
        password=os.environ.get('REDDIT_PASSWORD')
    )

    path = "/Comments.json"
    if os.path.exists(path):
        with open("Comments.json", "r") as jsonfile:
            data_object = json.load(jsonfile)
    else:
        data_object = []
    while True:
        try:
            for submission in reddit.subreddit(target_subreddit).new(limit=target_submission_count):
                if hasattr(submission, "selftext_html"):
                    soup = BeautifulSoup(submission.selftext_html, 'html.parser')
                    for link in soup.findAll('a', href=True):
                        if RedditBotHelpers.get_matches_from_link(link.attrs['href']):
                            if RedditBotHelpers.is_submission_id_present_in_list_of_dictionaries(str(submission.id),
                                                                                                 data_object):
                                raise SubmissionExistsException
                            data = {"href": link.attrs["href"], "submission_id": str(submission.id)}
                            print(str(data["href"] + " has not already been scraped, continuing"))
                            data_object.append(data)
                            print("data appended")
                            with open("Comments.json", "w") as jsonfile:
                                json.dump(data_object, jsonfile, indent=4)
                            print("json dumped")
                            break
        except SubmissionExistsException:
            print("Submission has already been registered")
        except Exception as e:
            print(e)
        finally:
            sleep(600)


if __name__ == "__main__":
    main()

# SCOPE CREEP
# Also raise an error if the submission is > 12 hours
