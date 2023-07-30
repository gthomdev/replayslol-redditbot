import re
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
        patterns = [
            r"https:\/\/www\.op\.gg\/summoners\/((?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)[\/])",
            r"https:\/\/(euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\.op\.gg\/summoners\/.+",
            r"https:\/\/u\.gg\/lol\/profile\/((?:euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2|euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)[\/])",
            r"https:\/\/blitz\.gg\/lol\/profile\/((?:euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2|euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)[\/])"
        ]

        for pattern in patterns:
            for link in self.links:
                match = re.search(pattern, link)
                if match:
                    matched_string = match.group(1).rstrip('/')  # remove trailing '/'
                    return matched_string.rstrip('12')  # Removing trailing 1 or 2 if present
        return None

    def _extract_summoner(self):
        patterns = [
            r"https:\/\/(?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\.op\.gg\/summoners\/(?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\/([^\/]+)(?:\/champions)?",
            r"https:\/\/www\.op\.gg\/summoners\/(?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\/([^\/]+)(?:\/champions)?",
            r"https:\/\/u\.gg\/lol\/profile\/(?:euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2)\/([^\/]+)(?:\/overview)?",
            r"https:\/\/blitz\.gg\/lol\/profile\/\w+\/([^\/]+)"
        ]
        for pattern in patterns:
            for link in self.links:
                match = re.search(pattern, link)
                if match:
                    return match.group(1).rstrip('/')
        else:
            return None

    def _extract_match_history_link(self):
        patterns = [r"https:\/\/www\.op\.gg\/summoners\/(euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\/([^\/]+)",
                    r"https:\/\/(euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\.op\.gg\/summoners\/.+",
                    r"https:\/\/u\.gg\/lol\/profile\/(euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2)\/([^\/]+)(?:\/overview)?",
                    r"https:\/\/blitz\.gg\/lol\/profile\/\w+\/([^\/]+)"]
        for pattern in patterns:
            for link in self.links:
                match = re.search(pattern, link)
                if match:
                    return link
        else:
            return None

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
            "created_utc": self.submission.created_utc,
            "region": self.region,
            "summoner": self.summoner
        })
