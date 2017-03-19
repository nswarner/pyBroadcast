#!/usr/bin/python3

from socket import socket


class pyBroadcast:

    msg = None
    port = None
    sock = None

    def __init__(self, msg='pyBroadcast', port=55255):
        assert(isinstance(port, int)), 'Argument "port" is not an int.'

        self.msg = msg
        self.port = port

    def __del__(self):
        pass

    def setup_broadcast(self, msg='pyBroadcast', port=55255):
        assert(isinstance(port, int)), 'Argument "port" is not an int.'

        self.msg = msg
        self.port = port

    def begin_broadcast(self):
        self.socket = socket(AF_INET, SOCK_DGRAM)


