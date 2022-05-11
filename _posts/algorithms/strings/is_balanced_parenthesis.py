
import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):

    brackets={')':'(',']':'[','}':'{'}
    l=0
    r=len(s)-1
    b=set("[]{}()")

    while l < r:
        if s[l] not in b:
            l +=1
        if s[r] not in b:
            r -= 1
        if s[l] != brackets[s[r]]:
            print("false")
            return
        l+=1
        r-=1

    print("true")
s ="{{()]a}}"

isBalanced(s)