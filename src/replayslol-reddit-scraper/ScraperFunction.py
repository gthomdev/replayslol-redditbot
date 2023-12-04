from RedditScraper import RedditScraper
from time import sleep
import time
from datetime import datetime
from datetime import timedelta


class ScraperFunction:

    def __init__(self, config, credentials):
        self.reddit_scraper = RedditScraper(config, credentials)
        self.queue_name = config['queue']['name']
        self.queue_host = config['queue']['host']
        self.function_interval = config['function']['scan-interval']
        self.postgres_connection_string = credentials.postgres_connection_string
        self.start_time = time.time()

    def run(self):
        while True:
            self.reddit_scraper.summoners_on_cooldown.clear()
            self.reddit_scraper.get_summoners_on_cooldown(self.postgres_connection_string)
            self.reddit_scraper.publish_submission_to_postgres(self.postgres_connection_string)
            print(
                f"{datetime.now().isoformat()}Z:Completed function iteration. Sleeping for {self.function_interval} seconds. Next iteration will start at {(datetime.now() + timedelta(seconds=self.function_interval)).isoformat()}")
            sleep(self.function_interval)
