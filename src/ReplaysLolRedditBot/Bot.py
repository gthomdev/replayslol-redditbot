import json
from time import sleep
import logging
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from Errors import SubmissionExistsException
from Helpers import get_praw_client_from_config, get_matches_from_link, \
    is_submission_id_present_in_list_of_dictionaries, configure_logger, get_submission_file_path, \
    initialise_submissions, get_reddit_configurations


def main():
    # Load config
    load_dotenv()
    configure_logger()
    target_subreddit, submission_limit, user_agent = get_reddit_configurations()
    reddit = get_praw_client_from_config()
    submission_file_path = get_submission_file_path()
    scraped_submissions = initialise_submissions(submission_file_path)
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
                            logging.info(str(data["href"] + " has not already been scraped, continuing"))
                            scraped_submissions.append(data)
                            logging.info(str(data["href"] + " appended"))
                            with open(submission_file_path, "w") as jsonfile:
                                json.dump(scraped_submissions, jsonfile, indent=4)
                            logging.info("Submission appended to Comments.json")
                            break
        except SubmissionExistsException:
            logging.info("Submission has already been registered")
        except Exception:
            raise
        finally:
            sleep(10)


if __name__ == "__main__":
    main()
