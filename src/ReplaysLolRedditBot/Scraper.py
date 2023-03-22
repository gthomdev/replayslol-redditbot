from ScraperFunction import ScraperFunction
from Helpers import load_config
from Credentials import Credentials

config = load_config("config.yaml")
print(f"Config Loaded: {config}")
credentials = Credentials()
print(f"Credentials Loaded: {credentials}")
scraper = ScraperFunction(config, credentials)

scraper.run()
