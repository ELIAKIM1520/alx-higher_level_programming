#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL """
import urllib.request
import urllib.parse
import sys


def post_email():
    """A python function that posts an email"""
    email_data = {'email': sys.argv[2]}
    email_data = urllib.parse.urlencode(email_data).encode('utf-8')

    with urllib.request.urlopen(sys.argv[1], email_data) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    post_email()
