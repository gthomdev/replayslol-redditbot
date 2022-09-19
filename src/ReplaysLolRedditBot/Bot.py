from time import sleep
import logging
from Errors import SubmissionExistsException
from Helpers import get_praw_client_from_config, get_submission_file_path, \
    initialise_submissions, get_reddit_configurations, initialise_application, get_links_for_subreddit


def main():
    initialise_application()
    target_subreddit, submission_limit, user_agent = get_reddit_configurations()
    reddit = get_praw_client_from_config()
    submission_file_path = get_submission_file_path()
    scraped_submissions = initialise_submissions(submission_file_path)
    while True:
        try:
            get_links_for_subreddit(reddit, scraped_submissions, submission_file_path, submission_limit,
                                    target_subreddit)
        except SubmissionExistsException:
            logging.info("Submission has already been registered")
        except Exception:
            raise
        finally:
            sleep(600)


if __name__ == "__main__":
    main()
