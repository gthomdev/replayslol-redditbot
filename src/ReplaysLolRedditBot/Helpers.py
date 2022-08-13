import re
from ReplaysLolRedditBot.Errors import InvalidOperationException

patterns = [
    "https?://(?:euw|na|oce|eune|br|jp|ru|tr){1}.op.gg/summoners?/(euw|na|oce|eune|br|jp|ru|tr)?/(.{3,16})",
    "https?://u.gg/lol/profile/(euw1|eune1|na1|tr1|br1|kr1|jp1|oce1|ru1)/(.{3,16})/(?:overview)?",
    "https?://blitz.gg/lol/profile/(euw1|eune1|na1|tr1|br1|kr1|jp1|oce1|ru1)/(.{3,16})/?"
]


def get_matches_from_link(text):
    for pattern in patterns:
        regex = re.compile(pattern)
        match_outcome = regex.search(text)
        if match_outcome:
            return match_outcome
    return None


def is_submission_id_present_in_list_of_dictionaries(submission_id, list_of_dictionaries):
    if len(list_of_dictionaries) == 0:
        raise InvalidOperationException
    for dictionary in list_of_dictionaries:
        if ("submission_id", str(submission_id)) in dictionary.items():
            return True
    return False
