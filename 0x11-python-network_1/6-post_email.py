#!/usr/bin/python3
""" post using requests """
import sys
import requests


def post_email():
    """function that takes in a URL and an email address, sends a POST"""
    email_string_data = {"email": sys.argv[2]}
    url_response = requests.post(sys.argv[1], data=email_string_data)
    print(url_response.text)


if __name__ == "__main__":
    post_email()
