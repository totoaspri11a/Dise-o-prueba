from sys import setrecursionlimit
from sys import stdin 

#Resuelto por el profesor Camilo Rocha en clase

setrecursionlimit(1<<24)

T,P = None, None

def phi_memo(n, m, memo):
  ans,key = None,(n, m)
  if key in memo: ans = memo[key]
  else:
    if m==0: 
      ans = 1
    elif m>n: 
      ans = 0
    else:
      ans = phi_memo(n-1, m, memo)
      if T[n-1]==P[m-1]:
        ans += phi_memo(n-1, m-1, memo)
    memo[key] = ans
  return ans

def main():
  global T, P
  N = int(stdin.readline())
  while N!=0:
    T = stdin.readline().strip()
    P = stdin.readline().strip()
    print(phi_memo(len(T), len(P), dict()))
    N-=1
main()
