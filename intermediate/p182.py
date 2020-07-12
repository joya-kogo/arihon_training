m = 10000
n = 2

def mat_mul(a,b):
	c = [[0 for j in range(len(b[0]))]for i in range(len(a))]
	for i in range(len(a)):
			for k in range(len(b)):
				for j in range(len(b[0])):
					c[i][j] = (c[i][j] + a[i][k]*b[k][j])%m
	return c


def mat_pow(a,n):
	b = [[0 for j in range(len(a))]for i in range(len(a))]
	for i in range(len(a)):
		b[i][i] = 1
	while (n > 0):
		if n&1:
			print("b")
			b = mat_mul(b, a)
			print(b)
		a = mat_mul(a,a)
		print("a")
		print(a)
		n = n >> 1
		print(n)
	return b

a = [[2,1,0],[2,2,2],[0,1,2]]
b = [[1],[0],[0]]

def solve():
	an = mat_pow(a,2)
	print(an[0][0])

solve()