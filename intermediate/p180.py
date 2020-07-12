m = 10000

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
			b = mat_mul(b, a)
		a = mat_mul(a,a)
		n = n >> 1
	return b

a = [[1,1],[1,0]]
b = [[1],[0]]

def solve():
	an = mat_pow(a,8)
	res = mat_mul(an,b)
	print(res[0][0])

solve()