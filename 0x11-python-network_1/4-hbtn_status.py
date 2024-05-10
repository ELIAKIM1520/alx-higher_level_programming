#!/usr/bin/python3
""" use requests """
import requests


def fetch_status():
    """function that fetches a status"""
    url_response = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type:", type(url_response.text))
    print("\t- content:", url_response.text)


if __name__ == "__main__":
    fetch_status()
