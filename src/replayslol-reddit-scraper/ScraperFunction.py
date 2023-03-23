from RedditScraper import RedditScraper
from time import sleep


class ScraperFunction:

    def __init__(self, config, credentials):
        self.reddit_scraper = RedditScraper(config, credentials)
        self.queue_name = config['queue']['name']
        self.queue_host = config['queue']['host']
        self.function_interval = config['function']['scan-interval']

    def run(self):
        while True:
            self.reddit_scraper.scrape_submissions()
            self.reddit_scraper.publish_submission(self.queue_name, self.queue_host)
            sleep(self.function_interval)
