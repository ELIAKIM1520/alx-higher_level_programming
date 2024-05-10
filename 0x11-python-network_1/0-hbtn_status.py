#!/usr/bin/python3
""" get content from a specified url """
import urllib.request


def status():
    """Python script that fetches https://alx-intranet.hbtn.io/status"""
    string_url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(string_url) as url_response:
        url_content = url_response.read()
        utf8_content = url_content.decode('utf-8')

        print("Body response:")
        print("\t- type:", type(url_content))
        print("\t- content:", url_content)
        print("\t- utf8 content:", utf8_content)


if __name__ == "__main__":
    status()
