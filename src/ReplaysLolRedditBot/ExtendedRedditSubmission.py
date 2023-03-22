import re
from bs4 import BeautifulSoup
from functools import cached_property
import json

class ExtendedRedditSubmission:
    def __init__(self, submission):
        self.submission = submission
        self.id = submission.id

    def __str__(self):
        return f"Submission ID: {self.submission.id}, Title: {self.submission.title}, Links: {self.links}"

    @cached_property
    def links(self):
        if self.attribute_is_not_empty('selftext_html'):
            return self._extract_links()
        else:
            return []

    def _extract_links(self):
        soup = BeautifulSoup(self.submission.selftext_html, 'html.parser')
        return [link.attrs['href'] for link in soup.findAll('a', href=True)]

    def attribute_is_not_empty(self, attr_name):
        return hasattr(self.submission, attr_name) and getattr(self.submission, attr_name) is not None

    def has_matching_link(self, patterns):
        return any(
            any(re.search(pattern, link) for pattern in patterns)
            for link in self.links)

    def to_json(self):
        return json.dumps({
            "submission_id": self.submission.id,
            "title": self.submission.title,
            "links": self.links,
            "author": self.submission.author.name,
            "created_utc": self.submission.created_utc
        })
