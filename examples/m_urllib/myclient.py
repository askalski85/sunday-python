#!/usr/bin/env python

import urllib
import sys

class UrllibSimpleClient:
    def __init__(self):
        print("Created myself")

    def simple_request(self, endpoint):
        print("Simple request to " + endpoint)
        urllib.urlopen("http://localhost:8019/hello.py/" + endpoint)
