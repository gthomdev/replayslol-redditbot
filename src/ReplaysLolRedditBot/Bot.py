import json
from time import sleep

from bs4 import BeautifulSoup
from dotenv import load_dotenv

from Errors import SubmissionExistsException
from Helpers import *


def main():
    load_dotenv()
    configuration = load_config_from_local_directory("config.yaml")
    target_subreddit = configuration['client']['target-subreddit']
    submission_limit = configuration['client']['submission-count']
    reddit = get_praw_client_from_config(configuration)
    path = "../../Comments.json"
    if os.path.exists(path):
        with open("../../Comments.json", "r") as jsonfile:
            scraped_submissions = json.load(jsonfile)
    else:
        scraped_submissions = []
    while True:
        try:
            for submission in reddit.subreddit(target_subreddit).new(limit=submission_limit):
                if hasattr(submission, 'selftext_html') and submission.selftext_html is not None:
                    soup = BeautifulSoup(submission.selftext_html, 'html.parser')
                    for link in soup.findAll('a', href=True):
                        if get_matches_from_link(link.attrs['href']):
                            if is_submission_id_present_in_list_of_dictionaries(str(submission.id),
                                                                                scraped_submissions):
                                raise SubmissionExistsException
                            data = {"href": link.attrs["href"], "submission_id": str(submission.id)}
                            print(str(data["href"] + " has not already been scraped, continuing"))
                            scraped_submissions.append(data)
                            print("data appended")
                            with open("../../Comments.json", "w") as jsonfile:
                                json.dump(scraped_submissions, jsonfile, indent=4)
                            print("json dumped")
                            break
        except SubmissionExistsException:
            print("Submission has already been registered")
        except Exception:
            raise
        finally:
            sleep(600)


if __name__ == "__main__":
    main()
