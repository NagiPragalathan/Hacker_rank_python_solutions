#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
def avg(*arg):
    sum_of_arg = sum([i for i in arg])
    return sum_of_arg/len(arg)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()