from sys import stdin

def solve(A):
	C_MaxProduct = A[0]
	C_MinProduct = None
	P_MaxProduct = A[0]
	P_MinProduct = A[0]
	ans = A[0]
	for i in range(1,len(A)):
		C_MaxProduct = max(P_MaxProduct*A[i],P_MinProduct*A[i],A[i])
		C_MinProduct = min(P_MaxProduct*A[i],P_MinProduct*A[i],A[i])
		ans = max(ans,C_MaxProduct)
		P_MaxProduct = C_MaxProduct
		P_MinProduct = C_MinProduct
	return ans

def main():
	numbers = stdin.readline().split()
	while(len(numbers)!=0):
		if numbers[len(numbers)-1] == '-999999':
			numbers.remove('-999999')
			print(solve(list(map(int,numbers))))
			numbers = None
			numbers = stdin.readline().split()
		else:
			numbers = numbers + stdin.readline().split()

main()