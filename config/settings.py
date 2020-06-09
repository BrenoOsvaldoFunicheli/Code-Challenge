# settings.py
from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os


class Environment:
    # OR, explicitly providing path to '.env'
    def __init__(self):
        load_dotenv()
        # env_path = Path('.') / '.env'
        # load_dotenv(dotenv_path=env_path)

    def get_app_key(self):
        return os.getenv("API_KEY")

    def get_base_url(self):
        return os.getenv("URL")

    def get_city_id(self):
        return os.getenv("CITY_ID")


if __name__ == '__main__':
    e= Environment()
    print(e.get_app_key())
    print(e.get_base_url())
    print(e.get_city_id())
