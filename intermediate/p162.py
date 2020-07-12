n = 4
a = [3,1,4,2]

max_n = 10
bit = [0]*max_n
n = 8

def sum(i):
	s = 0
	while(i > 0):
		s += bit[i]
		i -= i & -i
	return s

def add(i, x):
	while i <= n:
		bit[i] += x
		i += i & -i

def solve():
	ans = 0
	for i in range(len(a)):
		ans += (i - bit[a[i]])
		add(a[i], 1)
	return ans

print(solve())
