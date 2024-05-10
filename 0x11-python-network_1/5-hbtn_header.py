#!/usr/bin/python3
""" get X-Request-ID using requests """
import sys
import requests


def response_header_value():
    """Function sends a request to the URL and displays the value"""
    url_response = requests.get(sys.argv[1])

    if 'X-Request-Id' in url_response.headers:
        print(url_response.headers['X-Request-Id'])


if __name__ == "__main__":
    response_header_value()
