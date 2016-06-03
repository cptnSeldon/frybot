"""Debug"""
from conf.config import DEBUG


def print_debug(message):
    if DEBUG:
        print(message)
