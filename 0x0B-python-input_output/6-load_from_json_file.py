#!/usr/bin/python3
"""defining load_from_json_file function"""


import json


def load_from_json_file(filename):
    """creates an object from json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Priv
