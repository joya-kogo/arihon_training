n = 3
k = 2
t = [[2,2],[5,3],[2,1]]

def judge(m):
	c = list(map(lambda x:x[1]-m*x[0], t))
	c = sorted(c, reverse=True)
	print(c)
	s = 0
	for i in range(k,0,-1):
		s = s + c[i]
	if 0<=s:
		return True
	else:
		return False

def solve():
	ub = 3.0
	lb = 0.0
	while ub - lb > 1:
		mid = (ub + lb) /2
		if judge(mid):
			lb = mid
		else:
			ub = mid
	return lb

solve()