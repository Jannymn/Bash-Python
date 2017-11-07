#!/usr/bin/env python

#   Use script to create door.
#   E.g. Create socket listen data
#   Author Kol-zeng
#   Date 2017-10-27

import socket
import subprocess
import select
import sys


class Door():
    def __init__(self, port):
        self.port = port
        self.srvsock = -
