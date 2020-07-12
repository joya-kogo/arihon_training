n = 5
m = 3
x = [1,2,8,4,9]
x = sorted(x)
print(x)

def judge(d):
	now = x[0]
	count = 0
	for i in range(1, n):
		if d<=x[i] - now:
			now = x[i]
			count = count + 1
	if m-1 <= count:
		return True
	else:
		return False

def solve():
	# 全ての間隔がd以上
	ub = max(x)
	lb = 0
	while ub - lb > 1:
		mid = int((ub+lb)/2)
		print(mid, judge(mid))
		if judge(mid):
			lb = mid
		else:
			ub = mid
	return lb

print(solve())