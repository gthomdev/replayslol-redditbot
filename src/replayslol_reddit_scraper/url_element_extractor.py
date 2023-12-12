import re

REGION_PATTERNS = [
    r"https:\/\/www\.op\.gg\/summoner(?:s?)\/((?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)[\/])",
    r"https:\/\/(euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\.op\.gg\/summoners\/.+",
    r"https:\/\/u\.gg\/lol\/profile\/((?:euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2|euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)[\/])",
    r"https:\/\/blitz\.gg\/lol\/profile\/((?:euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2|euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)[\/])"]

SUMMONER_PATTERNS = [
    r"https:\/\/(?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\.op\.gg\/summoners\/(?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\/([^\/]+)(?:\/champions)?",
    r"https:\/\/www\.op\.gg\/summoner(?:s?)\/(?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\/([^\/]+)(?:\/champions)?",
    r"https:\/\/u\.gg\/lol\/profile\/(?:euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2)\/([^\/]+)(?:\/overview)?",
    r"https:\/\/blitz\.gg\/lol\/profile\/\w+\/([^\/]+)"]

MATCH_HISTORY_PATTERNS = [
    r"https:\/\/www\.op\.gg\/summoner(?:s?)\/(euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\/([^\/]+)",
    r"https:\/\/(euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\.op\.gg\/summoners\/.+",
    r"https:\/\/u\.gg\/lol\/profile\/(euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2)\/([^\/]+)(?:\/overview)?",
    r"https:\/\/blitz\.gg\/lol\/profile\/\w+\/([^\/]+)"]


class URLElementExtractor:
    def __init__(self):
        self.region_patterns = [re.compile(pattern) for pattern in REGION_PATTERNS]
        self.summoner_patterns = [re.compile(pattern) for pattern in SUMMONER_PATTERNS]
        self.match_history_link_patterns = [re.compile(pattern) for pattern in MATCH_HISTORY_PATTERNS]

    def extract_region(self, urls):
        if isinstance(urls, str):
            urls = [urls]

        for pattern in self.region_patterns:
            for url in urls:
                match = re.search(pattern, url)
                if match:
                    matched_string = match.group(1).rstrip('/')  # remove trailing '/'
                    return matched_string.rstrip('12')  # Removing trailing 1 or 2 if present
        return None

    def extract_summoner(self, urls):
        for pattern in self.summoner_patterns:
            for url in urls:
                match = re.search(pattern, url)
                if match:
                    return match.group(1).rstrip('/')
        else:
            return None

    def extract_match_history_link(self, urls):
        for pattern in self.match_history_link_patterns:
            for url in urls:
                match = re.search(pattern, url)
                if match:
                    return url
        else:
            return None
