import unittest
import re


def get_region(link):
    patterns = [
        r"https:\/\/www\.op\.gg\/summoners\/((?:euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)[\/])",
        r"https:\/\/(euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)\.op\.gg\/summoners\/.+",
        r"https:\/\/u\.gg\/lol\/profile\/((?:euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2|euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)[\/])",
        r"https:\/\/blitz\.gg\/lol\/profile\/((?:euw1|na1|kr1|oce1|jp1|br1|eune1|las1|lan1|tr1|ru1|sg1|ph1|tw1|vn1|th1|euw2|na2|kr2|oce2|jp2|br2|eune2|las2|lan2|tr2|ru2|sg2|ph2|tw2|vn2|th2|euw|na|kr|oce|jp|br|eune|las|lan|tr|ru|sg|ph|tw|vn|th)[\/])"
    ]
    for pattern in patterns:
        match = re.search(pattern, link)
        if match:
            matched_string = match.group(1).rstrip('/')  # remove trailing '/'
            return matched_string.rstrip('12')  # Removing trailing 1 or 2 if present
    return None


class RegionTestCases(unittest.TestCase):
    def test_manouche(self):
        result = get_region("https://euw.op.gg/summoners/euw/manouche%20zaatar")
        self.assertEqual("euw", result)  # add assertion here

    def test_long_name(self):
        result = get_region("https://www.op.gg/summoners/euw/%E4%B8%8D%E5%A5%BD%E6%84%8F%E6%80%9D")
        self.assertEqual("euw", result)


if __name__ == '__main__':
    unittest.main()
