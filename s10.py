# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 20:52:39 2022

@author: snikula
"""
def get_check_digit(num: int) -> int:
    """Get S10 check digit."""
    weights = [8, 6, 4, 2, 3, 5, 9, 7]
    sum = 0
    for i, digit in enumerate(f"{num:08}"):
        sum += weights[i] * int(digit)
    sum = 11 - (sum % 11)
    if sum == 10:
        sum = 0
    elif sum == 11:
        sum = 5
    print(("src = {0}, out = {1}")
          .format(num,sum))
    return sum

get_check_digit(12340167)
