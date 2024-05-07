import json

from dotenv import load_dotenv
from os import getenv
from pathlib import Path


def read_settings_file():
    settings_file = Path('./settings.ini')
    if settings_file.exists():
        with open('settings.ini', 'r') as f:
            data = f.read()
            if data:
                return json.loads(data)


load_dotenv()
settings = read_settings_file()
LOG_PATH = None

if getenv('LOG_PATH'):
    LOG_PATH = Path(getenv('LOGPATH'))
elif settings and settings['LOG_PATH']:
    LOG_PATH = Path(settings['LOG_PATH'])
