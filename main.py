#!/usr/bin/python3

import multiprocessing
import time

from broadcast import Broadcast
from receive import Receive


class Main:

    def __init__(self):
        raise RuntimeError("Cannot instantiate Main class.")

    @staticmethod
    def receiver():
        # Setup Receiver
        recv = Receive()
        data = recv.begin_receive(5)

    @staticmethod
    def broadcaster():
        # Give Receiver time to setup
        time.sleep(1)
        # Setup Broadcaster
        bcast = Broadcast()
        # Broadcast message
        bcast.broadcast("Broadcasting end")

if (__name__ == '__main__'):
    print("Running main.")

    recv_proc = multiprocessing.Process(target=Main.receiver)
    send_proc = multiprocessing.Process(target=Main.broadcaster)
    recv_proc.start()
    time.sleep(1)
    send_proc.start()