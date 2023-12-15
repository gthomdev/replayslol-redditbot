from url_element_extractor import URLElementExtractor
from bs4 import BeautifulSoup
from functools import cached_property
import json


class ExtendedRedditSubmission:
    def __init__(self, submission):
        self.submission = submission
        self.subreddit = submission.subreddit.display_name
        self.id = submission.id

    def __str__(self):
        return f"Submission ID: {self.submission.id}, Title: {self.submission.title}, Links: {self.links}"

    @cached_property
    def url(self):
        return self.submission.url

    @cached_property
    def links(self):
        if self.attribute_is_not_empty('selftext_html'):
            return self._extract_links()
        else:
            return []

    @cached_property
    def region(self):
        return self._extract_region()

    @cached_property
    def subreddit(self):
        return self.subreddit

    @cached_property
    def summoner(self):
        return self._extract_summoner()

    @cached_property
    def match_history_link(self):
        return self._extract_match_history_link()

    def _extract_region(self):
        return URLElementExtractor.extract_region(self.links)

    def _extract_summoner(self):
        return URLElementExtractor.extract_summoner(self.links)

    def _extract_match_history_link(self):
        return URLElementExtractor.extract_match_history_link(self.links)

    def _extract_links(self):
        soup = BeautifulSoup(self.submission.selftext_html, 'html.parser')
        return [link.attrs['href'] for link in soup.findAll('a', href=True)]

    def attribute_is_not_empty(self, attr_name):
        return hasattr(self.submission, attr_name) and getattr(self.submission, attr_name) is not None

    def has_matching_link(self):
        return URLElementExtractor.has_matching_link(self.links)

    def to_json(self):
        return json.dumps({
            "submission_id": self.submission.id,
            "title": self.submission.title,
            "links": self.links,
            "author": self.submission.author.name,
            "created_utc": self.submission.created_utc,
            "region": self.region,
            "summoner": self.summoner
        })
