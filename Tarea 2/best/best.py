#Uva problem 11658 - Coalitions
from cmath import pi
from sys import stdin
from unittest import result
import math

MAX = 10001

def main():
    personal = 0
    n,x = map(int,stdin.readline().split())
    dp = [_ for _ in range(MAX)]
    while n+x != 0:
        dp[0] = 1
        for i in range(1, MAX):
            dp[i] = 0
        x-=1
        for i in range(n):
            number = float(stdin.readline())
            q, p = math.modf(number)
            money = int(100 * p) + int(q)
            if i==x:
                personal = money
            else:
                for j in range(MAX-1, -1, -1):
                    if dp[j] > 0:
                        dp[j+money] = 1
        if personal > 5000:
            print("100.00")
        else:
            remaining = 5000 - personal
            for i in range(remaining + 1, MAX):
                if dp[i] > 0:
                    result = (100.00 * personal)/(personal+1)
                    print("{:.2f}".format(result))
                    break           
        n,x = map(int,input().split())

main()