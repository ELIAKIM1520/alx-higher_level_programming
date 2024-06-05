#!/usr/bin/python3
""" json api """
import requests
import sys


def search_api():
    """Write a Python script that takes in a letter and sends a POST"""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url_string = "http://0.0.0.0:5000/search_user"
    url_response = requests.post(url_string, data={'q': q})
    response_data = url_response.json()

    try:
        if response_data:
            print("[{}] {}".format(response_data['id'], response_data['name']))
        elif not response_data:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_api()
