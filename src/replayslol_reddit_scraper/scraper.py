from scraper_function import ScraperFunction
from helpers import load_config
from credentials import Credentials

config = load_config("config.yaml")
print(f"Config Loaded: {config}")
credentials = Credentials()
print(f"Credentials Loaded: {credentials}")
scraper = ScraperFunction(config, credentials)
scraper.run()
