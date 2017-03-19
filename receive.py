#!/usr/bin/python3

import ipaddress
import socket
import struct
from time import time

from logger import Logger


class Receive:

    sock = None
    port = None
    mcast_configuration = None
    multicast = None

    def __init__(self, multicast='239.1.1.222', port=55255):
        assert(isinstance(port, int)), 'Argument "port" is not an int.'
        try:
            ipaddress.ip_address(multicast)
        except:
            Logger.log("Receive: multicast argument is invalid.")
            raise

        self.port = port
        self.multicast = multicast
        Logger.log("Receive: Initialized Receive object.")

    def __del__(self):
        pass

    def setup_receive(self, multicast='239.1.1.222', port=55255):
        assert(isinstance(port, int)), 'Argument "port" is not an int.'
        try:
            ipaddress.ip_address(multicast)
        except:
            Logger.log("Receive: multicast argument is invalid when reinitializing Receive object.")
            raise

        self.port = port
        self.multicast = multicast
        Logger.log("Receive: Reinitialized Receive object.")

    def begin_receive(self, timeout=30):
        finished = False
        recvd = ""
        data = {}

        assert(isinstance(timeout, int)), 'Argument "timeout" must be an int.'

        Logger.log("Receive: Beginning receive process.")
        self.mcast_configuration = struct.pack('4sl', socket.inet_aton(self.multicast), socket.INADDR_ANY)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, self.mcast_configuration)
        self.sock.settimeout(3)
        self.sock.bind(('', self.port))
        Logger.log("Receive: Socket setup with multicast settings.")

        stime = time() + timeout
        Logger.log("Receive: Timeout set for " + str(stime))

        while(not finished):
            Logger.log("Attempting to receive data.")
            try:
                recv, addr = self.sock.recvfrom(1024)
                if (addr in data.keys()):
                    data[addr] += recv
                else:
                    data.update({addr:data})
                recvd += str(recv)
                Logger.log("Received [" + str(recv) + "] from " + str(addr))
            except socket.timeout as e:
                pass
            if (recvd[-4:-1] == 'end'):
                finished = True
                Logger.log("Received 'end' notifier. Cleaning up.")
            else:
                print(recvd[-3:] + "\n")
            if (stime < time()):
                finished = True
                Logger.log("Overran 'stime' without 'end' notifier.")

        return data


if (__name__ == '__main__'):
    recv = Receive()
    data = recv.begin_receive()

    print("Received: \n")
    print(str(data) + "\n")