#!/usr/bin/python3
""" get X-request-id from headers """
import urllib.request
import sys


def response_header_value():
    """sends a request to the URL and - displays the value"""
    with urllib.request.urlopen(sys.argv[1]) as url_response:
        if 'X-Request-Id' in url_response.headers:
            print(url_response.headers['X-Request-Id'])


if __name__ == "__main__":
    response_header_value()
