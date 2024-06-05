#!/usr/bin/python3
""" print http errors """
import sys
import urllib.request


def error_code():
    """ends a request to the URL and displays the body"""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    error_code()
