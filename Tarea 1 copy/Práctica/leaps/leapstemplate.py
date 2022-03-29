from sys import stdin
from math import sqrt,sin,cos,pi,floor

N,city = None,None
A,EPS = 9.8,1e-5

# https://stackoverflow.com/questions/29246455/python-setting-decimal-place-range-without-rounding
# def truncate(f, n): return floor(f * 10 ** n) / 10 ** n

def solve():
  ans = (-1,-1)
  return ans

def main():
  global N,city
  line = stdin.readline()
  while len(line)!=0:
    N,city = int(line),list()
    for _ in range(N):
      city.append(tuple(map(float,stdin.readline().split())))
    angle,vel = solve()
    print('{0:.2f} {1:.2f}'.format(angle, vel))
    line = stdin.readline()

main()
