import unittest
import re

def get_summoner(link):
    patterns = [
        r"https:\/\/(?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\.op\.gg\/summoners\/(?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\/([^\/]+)(?:\/champions)?",
        r"https:\/\/www\.op\.gg\/summoners\/(?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\/([^\/]+)(?:\/champions)?",
        r"https:\/\/u\.gg\/lol\/profile\/(?:euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2)\/([^\/]+)(?:\/overview)?",
        r"https:\/\/blitz\.gg\/lol\/profile\/\w+\/([^\/]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, link)
        if match:
            return match.group(1).rstrip('/')
    else:
        return None

en_us_link = "https://www.op.gg/summoners/na/Goated%20Tre?hl=en_US"
class SummonerTestCases(unittest.TestCase):
    def test_manouche(self):
        result = get_summoner("https://euw.op.gg/summoners/euw/manouche%20zaatar")
        self.assertEqual("manouche%20zaatar", result)

    def test_long_name(self):
        result = get_summoner("https://www.op.gg/summoners/euw/%E4%B8%8D%E5%A5%BD%E6%84%8F%E6%80%9D")
        self.assertEqual("%E4%B8%8D%E5%A5%BD%E6%84%8F%E6%80%9D", result)

    def test_with_forward_slash(self):
        result = get_summoner(r"https://www.op.gg/summoners/euw/Junko%20Challenger/champions")
        self.assertEqual("Junko%20Challenger", result)

    def test_en_us(self):
        result = get_summoner(en_us_link)
        self.assertEqual("Goated%20Tre", result)
if __name__ == '__main__':
    unittest.main()
