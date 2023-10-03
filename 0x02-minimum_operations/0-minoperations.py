#!/usr/bin/python3
"""
Minimum operations for CTRL + C and CTRL + V
"""


def minOperations(n):
    """
    Minimum Operations for CTRL + C and CTRL + V

    :param n:
    :return int:
    """
    if n <= 1:
        return 0
    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op
