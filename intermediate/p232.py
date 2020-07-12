import bisect

n = 5
xyr = [[0,-2,1],[0,3,3],[0,0,10],[0,1.5,1],[50,50,10]]

def search(arr, n, v):
	lb = -1
	ub = n
	while ub - lb > 1:
		mid = int((ub+lb)/2)
		if v <= arr[mid]:
			ub = mid
		else:
			lb = mid
	return lb, ub

def inside(i, j):
	if (xyr[i][0]-xyr[j][0])**2 + (xyr[i][1]-xyr[j][1])**2 <= xyr[j][2]**2:
		return 1
	else:
		return 0

def solve():
	x = []
	y = []
	r = []
	cs = []
	for i in range(n):
		x.append([xyr[i][0]-xyr[i][2], i, "l"])
		x.append([xyr[i][0]+xyr[i][2], i, "r"])
		y.append([xyr[i][1], i])
		r.append(xyr[i][2])
	x = sorted(x)
	y = sorted(y)
	ans = []
	for i in range(len(x)):
		iidx = x[i][1]
		if x[i][2] == "l":
			# print("円考慮中", iidx)
			lb, ub = search(cs, len(cs), [xyr[iidx][1], iidx])
			# print(cs)
			# print(lb, ub)
			res = 0
			if 2 <= len(cs):
				# print("aaaa", cs[lb], cs[ub], x[i])
				if lb != -1:
					# print("lb",inside(iidx, cs[lb][1]))
					res += inside(iidx, cs[lb][1])
				# print("ub",inside(iidx, cs[ub][1]))
				res += inside(iidx, cs[ub][1])
			elif 1 == len(cs):
				res += inside(iidx, cs[0][1])
			if res == 0:
				ans.append(iidx+1)
			idx = bisect.bisect_left(cs, [xyr[iidx][1], iidx])
			cs.insert(idx, [xyr[iidx][1], iidx])
			# print("inserted",cs)
		else:
			cs.remove([xyr[iidx][1], iidx])
			# m += 1
	# print(cs)
	# print(ans)
	return 


solve()