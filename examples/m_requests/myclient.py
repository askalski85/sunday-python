#!/usr/bin/env python

import requests
import sys

class RequestsSimpleClient:
    def __init__(self, server):
        self._server = server
        print("Created myself")

    def simple_request(self, endpoint):
        requests.get(self._server + endpoint)

    def get_response(self, endpoint):
        r = requests.get(self._server + endpoint)
        print(r.text, r.status_code)
        return "placeholder"
