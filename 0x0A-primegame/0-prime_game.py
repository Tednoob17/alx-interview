#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines the winner of each game"""
    if (not nums or x < 1):
        return None
    max_num = max(nums)
