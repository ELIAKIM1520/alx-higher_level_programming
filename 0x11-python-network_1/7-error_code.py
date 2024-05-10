#!/usr/bin/python3
""" get status code above 400 """
import sys
import requests


def error_code():
    url_response = requests.get(sys.argv[1])
    if url_response.status_code >= 400:
        print("Error code:", url_response.status_code)
    else:
        print(url_response.text)


if __name__ == "__main__":
    error_code()
