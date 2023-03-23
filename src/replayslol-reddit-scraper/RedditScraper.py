import praw
from replays_lol_reddit_scraper.ExtendedRedditSubmission import ExtendedRedditSubmission
import pika


class RedditScraper:
    def __init__(self, config, credentials):
        self.subreddit = config['reddit_client']['target-subreddit']
        self.submission_limit = config['reddit_client']['submission-limit']
        self.reddit = praw.Reddit(
            user_agent=config['reddit_client']['user-agent'],
            client_id=credentials.client_id,
            client_secret=credentials.client_secret,
            username=credentials.username,
            password=credentials.password
        )
        self.patterns = config['function']['patterns']
        self.checked_submissions = set()
        self.published_submissions = set()

    def scrape_submissions(self):
        for submission in self.reddit.subreddit(self.subreddit).new(limit=self.submission_limit):
            yield ExtendedRedditSubmission(submission)

    def validate_submissions(self):
        for submission in self.scrape_submissions():
            if submission.id not in self.checked_submissions and submission.id not in self.published_submissions:
                self.checked_submissions.add(submission.id)
                if submission.has_matching_link(self.patterns):
                    yield submission

    def publish_submission(self, queue_name, queue_host):
        connection = None
        channel = None

        for submission in self.validate_submissions():
            if submission.id not in self.published_submissions:
                if connection is None:
                    connection = pika.BlockingConnection(pika.ConnectionParameters(host=queue_host))
                    channel = connection.channel()
                try:
                    channel.basic_publish(exchange='', routing_key=queue_name, body=submission.to_json())
                    print(f"Published submission {submission.id} to queue: {queue_name} on host: {queue_host}")
                    self.published_submissions.add(submission.id)
                except Exception as e:
                    print(f"Error pushing submission {submission.id} to queue: {e}")

        if connection is not None:
            connection.close()
