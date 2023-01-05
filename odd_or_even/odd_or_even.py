#!/bin/python3

import math
import os
import random
import re
import sys


def check_odd_even(number):
    if(number%2 == 0):
        if (number>=2 and 5>=number):
            return "Not Weird"
        elif (number>=6 and 20>=number):
            return "Weird"
        elif(20<number):
            return 'Not Weird'
    else:
        return "Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(check_odd_even(n))
