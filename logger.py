#!/usr/bin/python3

from time import time


class Logger:

    def __init__(self):
        raise RuntimeError("Logger cannot be instantiated.")

    @staticmethod
    def log(msg, log_file='./app.log'):
        with open(log_file, 'a') as f:
            f.write(str(time()) + str(msg) + "\n")