import unittest
import RedditBotHelpers
import json


class LinkValidatorTests(unittest.TestCase):
    def setUp(self):
        with open("test_cases.json", "r") as file:
            self.test_cases = json.load(file)

    def test_correct_links_match_patterns(self):
        for test_case in self.test_cases:
            result = RedditBotHelpers.get_matches_from_link(test_case["link"])
            if test_case["is_none"]:
                self.assertIsNone(result)
                continue
            self.assertEqual(result.group(1), test_case["expected_results"]["groups"][0])
            self.assertEqual(result.group(0), test_case["expected_results"]["match"])
            self.assertEqual(result.group(2), test_case["expected_results"]["groups"][1])


class SubmissionDataObjectTests(unittest.TestCase):
    def setUp(self):
        self.data_object = [{'href': 'https://u.gg/lol/profile/na1/r3milo/overview', 'submission_id': 'wfj4lo'},
                            {'href': 'https://na.op.gg/summoners/na/imshmokinweed', 'submission_id': 'wfj4t2'}]
        self.present_submission_id = 'wfj4t2'
        self.absent_submission_id = 'abcd123'

    def test_should_return_true_if_submission_id_present_in_dictionary_keys(self):
        self.assertTrue(
            RedditBotHelpers.is_submission_id_present_in_list_of_dictionaries(self.present_submission_id,
                                                                              self.data_object))

    def test_should_return_false_if_submission_id_not_present_in_dictionary_keys(self):
        self.assertFalse(RedditBotHelpers.is_submission_id_present_in_list_of_dictionaries(self.absent_submission_id,
                                                                                           self.data_object)
                         )


if __name__ == '__main__':
    unittest.main()
