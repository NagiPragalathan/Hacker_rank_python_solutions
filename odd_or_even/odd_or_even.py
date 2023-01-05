#!/bin/python3

import math
import os
import random
import re
import sys


def check_odd_even(number):
    if(number%2 == 0):
        return "Not Weird"
    else:
        return "Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(check_odd_even(n))
