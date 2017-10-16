#!/usr/bin/env python3

import sys
from m_requests.myclient import RequestsSimpleClient
# from m_urllib.myclient   import UrllibSimpleClient
import logging

def main(args):
    server = args[1]
    print("Testing server", server)

    mySimpleClient = RequestsSimpleClient(server)
    # mySimpleClient.simple_request("/index")
    # mySimpleClient.simple_request("/sleep")
    mySimpleClient.get_response("/index")
    mySimpleClient.get_response("/sleep")

if __name__ == "__main__":
    print(sys.argv)
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    # requests_log = logging.getLogger("requests.packages.urllib3")
    # requests_log.setLevel(logging.DEBUG)
    # requests_log.propagate = True
    sys.exit(main(sys.argv))
