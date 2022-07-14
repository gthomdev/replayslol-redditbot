import unittest
import RedditBotHelpers


class LinkValidatorTests(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {
                "case": "correct_op_gg_link",
                "link": r'https://na.op.gg/summoners/na/JeffLynne',
                "is_none": False,
                "expected_results": {
                    "match": "https://na.op.gg/summoners/na/JeffLynne",
                    "groups": [
                        "na",
                        "JeffLynne"
                    ]
                }
            },
            {
                "case": "correct_u_gg_link",
                "link": r'https://na.op.gg/summoners/na/JeffLynne',
                "is_none": False,
                "expected_results": {
                    "match": "https://na.op.gg/summoners/na/JeffLynne",
                    "groups": [
                        "na",
                        "JeffLynne"
                    ]
                }
            },
            {
                "case": "correct_blitz_gg_link",
                "link": r'https://blitz.gg/lol/profile/euw1/JeffLynne',
                "is_none": False,
                "expected_results": {
                    "match": "https://blitz.gg/lol/profile/euw1/JeffLynne",
                    "groups": [
                        "euw1",
                        "JeffLynne"
                    ]
                }
            },
            {
                "case": "incomplete_blitz_gg_link",
                "link": r'https://blitz.gg/lol',
                "is_none": True,
            }
        ]

    def test_correct_links_match_patterns(self):
        for test_case in self.test_cases:
            result = RedditBotHelpers.is_target_link_type(test_case["link"])
            if test_case["is_none"]:
                self.assertIsNone(result)
                continue
            self.assertEqual(result.group(0), test_case["expected_results"]["match"])
            self.assertEqual(result.group(1), test_case["expected_results"]["groups"][0])
            self.assertEqual(result.group(2), test_case["expected_results"]["groups"][1])


if __name__ == '__main__':
    unittest.main()
