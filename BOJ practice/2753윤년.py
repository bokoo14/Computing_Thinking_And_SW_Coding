'''
import sys
input=sys.stdin.readline

year=int(input())

answer=0
if year%4==0 and year%100!=0:
    answer=1
elif year%400==0:
    answer=1
else:
    answer=0

print(answer)
'''

import sys
input=sys.stdin.readline

def isYear(y):
    return (y%4==0 and y%100!=0) or (y%400==0)

year=int(input())
print(1 if isYear(year) else 0)
