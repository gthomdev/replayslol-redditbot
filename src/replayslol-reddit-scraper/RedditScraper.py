import praw
from ExtendedRedditSubmission import ExtendedRedditSubmission
import pika
import psycopg2
from psycopg2 import sql
import time
from datetime import datetime, timedelta

class RedditScraper:
    def __init__(self, config, credentials):
        self.subreddits = config['reddit_client']['target-subreddit']
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
        self.summoners_on_cooldown = set()

    def get_summoners_on_cooldown(self, connection_string):
        connection = None
        cursor = None
        try:
            connection = psycopg2.connect(connection_string)
            cursor = connection.cursor()
            interval = datetime.now() - timedelta(hours=24)
            query = sql.SQL("""SELECT submission_id FROM reddit_comments WHERE created_at >= %s""")
            cursor.execute(query, (interval,))
            stale_submissions = cursor.fetchall()
            if len(stale_submissions) > 0:
                stale_submission_ids = [submission[0] for submission in stale_submissions]
                for stale_submission_id in stale_submission_ids:
                    self.published_submissions.add(stale_submission_id)
            query = sql.SQL("""SELECT summoner_name FROM reddit_comments WHERE created_at >= %s""")
            cursor.execute(query, (interval,))
            summoners_on_cooldown = cursor.fetchall()
            if len(summoners_on_cooldown) > 0:
                summoners_names_on_cooldown = [summoner[0] for summoner in summoners_on_cooldown]
                for summoner_name in summoners_names_on_cooldown:
                    self.summoners_on_cooldown.add(summoner_name)

        except Exception as e:
            print(f"Error getting stale submissions from database: {e.with_traceback()}")
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
    def scrape_submissions(self, maximum_age=1200):
        current_time = time.time()
        for subreddit in self.subreddits:
            print(f"Checking subreddit: {subreddit}")
            try:
                for submission in self.reddit.subreddit(subreddit).new(limit=self.submission_limit):
                    if current_time - submission.created_utc <= maximum_age:
                     yield ExtendedRedditSubmission(submission)
            except Exception as e:
                print(f"Error scraping subreddit {subreddit}: {e}")
    def validate_submissions(self):
        for submission in self.scrape_submissions():
            if submission.id not in self.checked_submissions and submission.id not in self.published_submissions and submission.summoner not in self.summoners_on_cooldown:
                self.checked_submissions.add(submission.id)
                self.summoners_on_cooldown.add(submission.summoner)
                if submission.has_matching_link(self.patterns):
                    print(f"Found matching submission: {submission.url}")
                    yield submission

    def publish_submission_to_queue(self, queue_name, queue_host):
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

    def publish_submission_to_postgres(self, connection_string):
        connection = None
        cursor = None

        try:
            connection = psycopg2.connect(connection_string)
            cursor = connection.cursor()
            for submission in self.validate_submissions():
                try:
                    if submission.id not in self.published_submissions:
                        if submission.region is None:
                            exception = Exception(f"Submission {submission.id} has no region.")
                            raise exception
                        if submission.summoner is None:
                            exception = Exception(f"Submission {submission.id} has no summoner.")
                            raise exception
                        if submission.match_history_link is None:
                            exception = Exception(f"Submission {submission.id} has no match history link.")
                            raise exception
                        # Insert the submission into the database
                        insert_query = "INSERT INTO reddit_comments (subreddit, region, summoner_name, submission_id, link, reddit_link) VALUES (%s, %s, %s, %s, %s, %s)"
                        values = (submission.subreddit, submission.region, submission.summoner, submission.id, submission.match_history_link, submission.url)
                        cursor.execute(insert_query, values)
                        print(f'Submission has subreddit: {submission.subreddit}')
                        print(f"Published submission {submission.id} to database.")
                        self.published_submissions.add(submission.id)
                except Exception as e:
                            print(f"Error inserting submission {submission.id} to database: {e}")
                # Commit the transaction to persist the changes
                connection.commit()

        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"Error connecting to the database: {e}")

        finally:
            # Close the cursor and connection
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()