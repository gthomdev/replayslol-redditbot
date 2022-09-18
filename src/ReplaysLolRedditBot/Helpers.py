import os
import re
import logging
import praw
import json
import yaml
from datetime import datetime

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
    for dictionary in list_of_dictionaries:
        if ("submission_id", str(submission_id)) in dictionary.items():
            return True
    return False


def get_praw_client_from_config():
    configuration = load_config(os.path.join(os.getcwd(), "config.yaml"))
    return praw.Reddit(
        user_agent=configuration['client']['user-agent'],
        client_id=os.environ.get('REDDIT_CLIENT_ID'),
        client_secret=os.environ.get('REDDIT_CLIENT_SECRET'),
        username=os.environ.get('REDDIT_USERNAME'),
        password=os.environ.get('REDDIT_PASSWORD')
    )


def load_config(file_path):
    configuration = yaml.safe_load(open(file_path))
    return configuration


def configure_logger():
    environment = os.environ.get('ENVIRONMENT')
    if environment == "development":
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    else:
        date = datetime.now().strftime("%Y-%m-%d-%I-%M-%S")
        path = os.getcwd()
        logging.basicConfig(filename=f'{path}/logs/{date}.log', format='%(asctime)s - %(message)s',
                            level=logging.INFO, datefmt="%Y-%m-%d-%I-%M-%S %z")


def get_submission_file_path():
    return os.path.join(os.getcwd(), "submissions.json")


def initialise_submissions(submission_file_path):
    if os.path.exists(submission_file_path):
        with open(submission_file_path, "r") as jsonfile:
            scraped_submissions = json.load(jsonfile)
    else:
        scraped_submissions = []
    return scraped_submissions


def get_reddit_configurations():
    reddit_config_directory = os.path.join(os.getcwd(), "config.yaml")
    configuration = load_config(reddit_config_directory)
    return (configuration['client']['target-subreddit'], configuration['client']['submission-limit'],
            configuration['client']['user-agent'])
