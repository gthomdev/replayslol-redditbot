import json
import os

import pytest
from ReplaysLolRedditBot.Helpers import get_matches_from_link, is_submission_id_present_in_list_of_dictionaries, \
    initialise_submissions


@pytest.fixture
def load_json_config():
    # os.path.join necessary because of different working dirs of packages calling this file, see
    # https://stackoverflow.com/questions/44652995/python-tox-no-such-file-or-directory-error
    with open(os.path.join(os.path.dirname(__file__), "test_cases.json"), "r") as config:
        return json.load(config)


def test_correct_links_match_patterns(load_json_config):
    for test_case in load_json_config:
        result = get_matches_from_link(test_case["link"])
        if test_case["is_none"]:
            assert result is None
            continue
        assert result.group(1) == test_case["expected_results"]["groups"][0]
        assert result.group(0) == test_case["expected_results"]["match"]
        assert result.group(2) == test_case["expected_results"]["groups"][1]


@pytest.fixture
def get_data_object():
    return [{'href': 'https://u.gg/lol/profile/na1/r3milo/overview', 'submission_id': 'wfj4lo'},
            {'href': 'https://na.op.gg/summoners/na/imshmokinweed', 'submission_id': 'wfj4t2'}]


@pytest.fixture
def get_present_submission_id(get_data_object):
    return get_data_object[0]["submission_id"]


@pytest.fixture
def get_absent_submission_id():
    return "abcd1234"


@pytest.fixture
def get_empty_data_object():
    return []


def test_should_return_true_if_submission_id_present_in_dictionary_keys(get_present_submission_id, get_data_object):
    assert is_submission_id_present_in_list_of_dictionaries(get_present_submission_id, get_data_object) is True


def test_should_return_false_if_submission_id_not_present_in_dictionary_keys(get_absent_submission_id, get_data_object):
    assert is_submission_id_present_in_list_of_dictionaries(get_absent_submission_id, get_data_object) is False


def test_initialise_submissions_should_return_empty_array_if_file_doesnt_exist():
    assert initialise_submissions("nonexistentfile.nerf") == []


def test_initialise_submissions_should_return_empty_array_if_file_is_empty():
    assert initialise_submissions("emptyfile.txt") == []


def test_initialise_submissions_should_return_array_if_file_exists_and_is_not_empty(get_data_object):
    assert initialise_submissions(os.path.join(os.path.dirname(__file__), "test_data.json")) == get_data_object
