#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """Determines the fwst number of coins needed to meet a given amnt total"""
    if (total <= 0):
        return 0
    if (coins is None or len(coins) == 0):
        return -1
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if (total <= 0):
            break
        num_coins += total // coin
        total = total % coin
    if (total != 0):
        return -1
    return num_coins
