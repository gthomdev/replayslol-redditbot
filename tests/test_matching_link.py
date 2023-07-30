import unittest
import re


def has_matching_link(links, list_of_patterns):
    return any(
        any(re.search(pattern, link) for pattern in list_of_patterns)
        for link in links)


patterns = [
    "https?://(?:www\.)?(?:(?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\\.)?op\\.gg/summoner(s)?/(?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)?/(.{3,16})",
    "https?://u.gg/lol/profile/(euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2|euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)/(.{3,16})(?:/overview)?",
    "https?://blitz.gg/lol/profile/(euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2|euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)/(.{3,16})/?"]

kr_link = "https://www.op.gg/summoners/kr/%EB%8C%95%EC%B2%AD%EC%9E%87"
euw_link = "https://euw.op.gg/summoners/euw/manouche%20zaatar"
eune_link = "https://www.op.gg/summoners/eune/joona5"
na_link = "https://www.op.gg/summoners/na/FLY%20VicLa"
sg_link = "https://www.op.gg/summoners/sg/%E6%9C%88%E6%86%94%E6%86%94%E5%A4%A7%E7%BE%8E%E5%A5%B3"
ph_link = "https://www.op.gg/summoners/ph/Mafumafu"
br_link = "https://www.op.gg/summoners/br/twitch%20nicklink"
oce_link = "https://www.op.gg/summoners/oce/LV1%20Daystar"
recon_link = "https://www.op.gg/summoners/na/Recon419A"
en_us_link = "https://www.op.gg/summoners/na/Goated%20Tre?hl=en_US"


class MatchingLinksTestCases(unittest.TestCase):

    def test_kr(self):
        self.assertEqual(True, has_matching_link([kr_link], patterns))

    def test_euw(self):
        self.assertEqual(True, has_matching_link([euw_link], patterns))

    def test_eune(self):
        self.assertEqual(True, has_matching_link([eune_link], patterns))

    def test_na(self):
        self.assertEqual(True, has_matching_link([na_link], patterns))

    def test_sg(self):
        self.assertEqual(True, has_matching_link([sg_link], patterns))

    def test_ph(self):
        self.assertEqual(True, has_matching_link([ph_link], patterns))

    def test_br(self):
        self.assertEqual(True, has_matching_link([br_link], patterns))

    def test_oce(self):
        self.assertEqual(True, has_matching_link([oce_link], patterns))

    def test_recon(self):
        self.assertEqual(True, has_matching_link([recon_link], patterns))

    def test_en_us(self):
        self.assertEqual(True, has_matching_link([en_us_link], patterns))

if __name__ == '__main__':
    unittest.main()
