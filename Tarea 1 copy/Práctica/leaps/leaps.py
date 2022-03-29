#Problem 10372 - Leaps


from sys import stdin
from math import sqrt,sin,cos,pi,floor

h,d = [ 0 for _ in range(102) ], [ 0 for _ in range(102) ]
a,EPS = 9.8,1e-5

# https://stackoverflow.com/questions/29246455/python-setting-decimal-place-range-without-rounding
# def truncate(f, n): return floor(f * 10 ** n) / 10 ** n

def solve(n):
    for i in range(1, 9000):
        angle = pi*i/18000
        vel = sqrt(a*d[n-1]/sin(2*angle))
        vx = vel*cos(angle)

        vy = vel*sin(angle)
        for j in range(1, n-1):

            t = d[j-1]/vx
            h1 = t*(vy-a*t/2)
            if (h1<h[j]): 
                break

            t = d[j]/vx
            h2 = t*(vy-a*t/2)
            if (h1<h[j]):
                break
            if j==n-1:
                break
    return i/100, vel

def main():
    line = stdin.readline()
    while len(line)!=0:
        n, tmp = int(line), list()
        for i in range(n):
            tmp.append(tuple(map(float,stdin.readline().split())))
            h[i],d[i] = tmp[i][0], tmp[i][1]
            if i>0:
                h[i] += d[i-1]
        ans1, vel = solve(n)
        print("{:.2f} {:.2f}".format(ans1, vel))
        line = stdin.readline()

main()