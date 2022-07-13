import unittest
import RedditBotHelpers


class LinkValidatorTests(unittest.TestCase):
    def setUp(self):
        self.u_gg_link = r'https://na.op.gg/summoners/na/JeffLynne'
        self.op_gg_link = r'https://na.op.gg/summoners/na/JeffLynne'
        self.blitz_gg_link = r'https://blitz.gg/lol/profile/euw1/JeffLynne'

    def u_gg_link_should_match_pattern(self):
        self.assertIsNotNone(RedditBotHelpers.is_target_link_type(self.u_gg_link))

    def op_gg_link_should_match_pattern(self):
        self.assertIsNotNone(RedditBotHelpers.is_target_link_type(self.op_gg_link))

    def blitz_gg_link_should_match_pattern(self):
        self.assertIsNotNone(RedditBotHelpers.is_target_link_type(self.blitz_gg_link))


if __name__ == '__main__':
    unittest.main()
