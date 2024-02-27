#!/usr/bin/python3
"""0-making_change.py"""

def makeChange(coins, total):
    """
    Returns fewest coins needed to meet total.
    If total <= 0, return 0.
    If total can't be met by coins, return -1.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
    return -1
