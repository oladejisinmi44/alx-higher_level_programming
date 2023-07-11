#!/usr/bin/python3
"""
This module supplies the function "load_from_json_file".
"""


import json


def load_from_json_file(filename):
    """
    This is a function that creates an Object from a “JSON file”
    """

    with open(filename, encoding="UTF-8") as fd:
        js = fd.read()
    return json.loads(js)
