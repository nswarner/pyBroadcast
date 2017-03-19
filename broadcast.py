#!/usr/bin/python3

import ipaddress
import socket
import struct

from logger import Logger


class Broadcast:

    msg = None
    port = None
    sock = None
    multicast = None

    def __init__(self, multicast='239.1.1.222', port=55255):
        assert(isinstance(port, int)), 'Argument "port" is not an int.'
        try:
            ipaddress.ip_address(multicast)
        except:
            Logger.log("Broadcast: multicast argument is invalid when reinitializing Receive object.")
            raise

        self.port = port
        self.multicast = multicast

    def __del__(self):
        pass

    def setup_broadcast(self, multicast='239.1.1.222', port=55255):
        assert(isinstance(port, int)), 'Argument "port" is not an int.'

        self.port = port
        try:
            ipaddress.ip_address(multicast)
        except:
            Logger.log("Broadcast: multicast argument is invalid when reinitializing Receive object.")
            raise

    def broadcast(self, msg="pyBroadcast"):
        end_point = (self.multicast, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        time_to_live = struct.pack('b', 1)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, time_to_live)

        Logger.log("Broadcast: Setup and attempting broadcast.")
        amt_sent = self.sock.sendto(str.encode(msg), end_point)

        Logger.log("Broadcast: Sent out [" + str(amt_sent) + "].")
