#!/usr/bin/python3
"""Log parsing"""
import sys


def print_stats(status_codes, file_size):
    """Prints the statistics"""
    print("File size: {}".format(file_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))
