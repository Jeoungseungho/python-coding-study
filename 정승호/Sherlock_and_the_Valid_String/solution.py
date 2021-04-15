import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    freq = {}
    cnt = set()
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else : 
            freq[ch] = 1
    
    for num in freq.values():
        cnt.add(num)
    
    if len(cnt) == 1:
        return 'YES'
    
    elif len(cnt) > 2:
        return 'NO'
    
    else:
        for key in freq:
            freq[key] -= 1
            temp = list(freq.values())
            try:
                temp.remove(0)
            except:
                pass
            if len(set(temp)) == 1:
                return 'YES'
            else :
                freq[key]+=1
    return 'NO' 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
