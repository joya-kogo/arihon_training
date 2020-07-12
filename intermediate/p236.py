import copy
m = 4
n = 3
x1y1 = [[7,2],[3,3],[0,2],[3,1]]
x2z2 = [[4,2],[0,1],[8,1]]

def width(ns, x):
	if ns == m:
		sh = x1y1
	else:
		sh = x2z2
	lb = float("inf")
	ub = -float("inf")
	# 本来は点の打ち方の規則性を確かめないと下のようには書けない...蟻本のミスかも
	# 点の順番がサークルになっている前提
	for i in range(ns):
		x1 = sh[i][0]
		x2 = sh[(i+1)%ns][0]
		y1 = sh[i][1]
		y2 = sh[(i+1)%ns][1]
		a = (y2-y1)/(x2-x1)
		b = y1 - a * x1
		y = a * x + b
		if y1 <= y and y <= y2 or y2 <= y and y <= y1:
			lb = min(y, lb)
			ub = max(y, ub)
	return ub - lb



def solve():
	xs = []
	for i in range(m):
		xs.append(x1y1[i][0])
	for i in range(n):
		xs.append(x2z2[i][0])
	xs = sorted(xs)
	xs = xs[0:6]
	res = 0
	for i in range(len(xs)-1):
		a = xs[i]
		b = xs[i+1]
		c = (a+b)/2
		sq1 = width(m, a) * width(n, a)
		sq2 = width(m, b) * width(n, b)
		sq3 = width(m, c) * width(n, c)
		res += (b-a)*(sq1 + sq2 + 4*sq3)/6
	return

solve()