from sys import stdin

INF = float('inf')


def fmax(x,y):
	if x[0] > y[0]:
		return x
	elif x[0] == y[0]:
		if  x[1] > y[1]:
			return x
		else:
			return y
	else:
		return y

def solve(limit, petra, jan):
	for i in range(1,n+1):
			limit = (i+1)//2
			for j in range(limit + 1):
				TAB[i][j][0] = TAB[i-1][j][0]		
				TAB[i][j][1] = TAB[i-1][j][1] + P[i][0]
				if(j > 0 ):
					TAB[i][j] = fmax(TAB[i][j],[P[i][1] + TAB[i-1][j-1][0],TAB[i-1][j-1][1]])
		
	petra += TAB[n][(n+1)//2][1] 
	jan = TAB[n][(n+1)//2][0]
	print(petra,jan)


def main():
	global n, P, TAB
	t = int(stdin.readline().strip())
	for _ in range(t):
		P = [[INF,INF]]
		n = int(stdin.readline().strip())
		name = stdin.readline().strip()
		petra = 0;jan = 0
		for _ in range(n):
			pi,ji = map(int,stdin.readline().split())
			P.append([pi,ji])
		
		P.sort(key = lambda x : (-x[0],x[1]))
		P[0] = [0,0]		
		if(name[0] == 'P'):
			petra = P[1][0]
			del P[1]
			n-=1
		TAB = [[[0,0] for _ in range((n//2)+2)] for _ in range(n+3)]
		limit = 0
		solve(limit, petra, jan)

main()