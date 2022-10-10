from time import sleep
import logging
from ReplaysLolRedditBot.Errors import SubmissionExistsException
from ReplaysLolRedditBot.Helpers import get_praw_client_from_config, get_submission_file_path, \
    initialise_submissions, get_reddit_configurations, initialise_application, get_links_for_subreddit, \
    post_submissions_to_submission_api


def main():
    initialise_application()
    target_subreddit, submission_limit, user_agent, scan_interval = get_reddit_configurations()
    reddit = get_praw_client_from_config()
    submission_file_path = get_submission_file_path()
    scraped_submissions = initialise_submissions(submission_file_path)
    while True:
        try:
            submissions = get_links_for_subreddit(reddit, scraped_submissions, submission_file_path, submission_limit,
                                                  target_subreddit)
            post_submissions_to_submission_api(submissions)
        except SubmissionExistsException:
            logging.info("Submission has already been registered")
        except Exception:
            raise
        finally:
            sleep(scan_interval)


if __name__ == "__main__":
    main()
