import re

patterns = [
    "(http)s?(://)(euw|na|oce|eune|br|jp|ru|tr)?(.op.gg/summoner)s?/(euw|na|oce|eune|br|jp|ru|tr)?(/userName=)?/.{3,16}",
    "(https)s?(://)(u.gg/lol/profile/)(euw1|eune1|na1|tr1|br1|kr1|jp1|oce1|ru1)/.{3,16}(/overview)",
    "(https)s?(://)(blitz.gg/lol/profile/)(euw1|eune1|na1|tr1|br1|kr1|jp1|oce1|ru1)/.{3,16}"
]


def is_target_link_type(text):
    for pattern in patterns:
        regex = re.compile(pattern)
        match_outcome = regex.search(text)
        if match_outcome:
            return match_outcome
    return None
