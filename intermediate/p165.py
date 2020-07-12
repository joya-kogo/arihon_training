max_n = 10
bit0 = [0]*max_n
bit1 = [0]*max_n
query = [[2,4,2,"c"],[2,4,"",""]]
n = 8

def sum(bit, i):
	s = 0
	while(i > 0):
		s += bit[i]
		i -= i & -i
	return s

def add(bit, i, x):
	while i <= n:
		bit[i] += x
		i += i & -i


def solve():
	add(bit0,1,5)
	add(bit0,2,3)
	add(bit0,3,7)
	add(bit0,4,9)
	add(bit0,5,6)
	add(bit0,6,4)
	add(bit0,7,1)
	add(bit0,8,2)
	for q in query:
		if q[3] == "c":
			l = q[0]
			r = q[1]
			x = q[2]
			add(bit0, l, -x*(l-1))
			add(bit1, l, x)
			add(bit0, r+1, x*r)
			add(bit1, r+1, -x)
		else:
			print(bit0)
			print(bit1)
			print(sum(bit1, q[1])*q[1]+sum(bit0,q[1]))

solve()