import math

n = 4
k = 11
l = [8.02, 7.43, 4.57, 5.39]

def solve():
	ub = int(max(l))
	lb = 0
	for j in range(100):
		mid = int((ub+lb)/2)
		print(mid)
		count = 0
		for i in range(n):
			count = count + math.floor(l[i]/mid)
			print(l[i], count)
		if k <= count:
			print("a")
			lb = mid
		else:
			ub = mid
	return lb

print(solve())