import logging
import json

logger = logging.getLogger(__name__)

raw_config = {}


def read_config(file):
    global raw_config
    with open(file) as json_file:
        raw_config = json.load(json_file)
        verify_config()


def verify_config():
    try:
        get_telegram_key()
    except KeyError as e:
        logger.error('key %s is required' % (e))


def get_telegram_key():
    global raw_config
    return raw_config["telegram_key"]
