m = 10000
n = 2
k = 2

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

a = [[0,1],[1,1]]
b = [[1,0],[0,1]]

def solve():
	ad = [[0 for i in range(2*n)] for j in range(2*n)]
	for i in range(n):
		for j in range(n):
			ad[i][j] = a[i][j]
		ad[i+n][i] = 1
		ad[i+n][i+n] = 1
	c = mat_pow(ad, k+1)
	d = mat_mul(c,b)
	d = d[2:]
	for i in range(n):
		for j in range(n):
			if i == j:
				d[i][j] = d[i][j] - 1
	print(d)
solve()