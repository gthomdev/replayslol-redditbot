import os
from dotenv import load_dotenv


class Credentials:
    def __init__(self):
        load_dotenv()
        self.client_id = os.environ.get('REDDIT_CLIENT_ID')
        self.client_secret = os.environ.get('REDDIT_CLIENT_SECRET')
        self.username = os.environ.get('REDDIT_USERNAME')
        self.password = os.environ.get('REDDIT_PASSWORD')
        self.postgres_connection_string = os.environ.get('POSTGRES_URL')
