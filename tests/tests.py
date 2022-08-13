import pytest
import json
from ReplaysLolRedditBot.Helpers import *
from ReplaysLolRedditBot.Errors import *


@pytest.fixture
def load_json_config():
    with open("tests/test_cases.json", "r") as config:
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


def test_should_throw_invalidoperationexception_if_collection_is_empty(get_present_submission_id,
                                                                       get_empty_data_object):
    with pytest.raises(InvalidOperationException):
        is_submission_id_present_in_list_of_dictionaries(get_present_submission_id, get_empty_data_object)
