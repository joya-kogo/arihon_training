import math
import copy
n = 7
m = 3
a = [1,5,2,6,3,7,4]
query = [[4,4,1]]


def bucket():
	bucket = []
	bidx = []
	b = int(math.sqrt(n))
	print(b)
	bnum = int(n/b)
	print(bnum)
	for i in range(bnum):
		bb = []
		bi = []
		for j in range(b):
			bb.append(a[i*2+j])
			bi.append(i*2+j)
		# 事前にソートしない
		# bb = sorted(bb)
		bucket.append(copy.deepcopy(bb))
		bidx.append(copy.deepcopy(bi))
	return bucket, bidx


def bsearch(arr, x):
	# if x<=arr[-1]:
	# 	return len(arr)
	# if arr[0] < x:
	# 	return 0
	ub = len(arr)
	lb = -1
	while ub-lb > 1:
		mid = int((ub+lb)/2)
		if arr[mid] <= x:
			lb = mid
		else:
			ub = mid
	return lb + 1

def solve():
	bc, bidx = bucket()
	print(bidx)
	b =int(math.sqrt(n))
	for q in query:
		ub = max(a)*2
		lb = 0
		while ub - lb > 1:
			num = 0
			x = int((ub+lb)/2)
			# x = 5
			print("x", x)
			l = q[0]-1
			print(l)
			r = q[1]
			print(r)
			if l % b != 0:
				while l%b != 0:
					if a[l] <= x:
						print("l", l)
						num = num + 1
					l = l + 1
			if r % b != 0:
				while r%b != 0:
					if a[r-1] <= x:
						print("r", r)
						num = num + 1
					r = r - 1
			print("hani", l, r-1)
			for i in range(len(bidx)):
				if l<=bidx[i][0] and bidx[i][1]<=r-1:
					print("i", i)
					arr = sorted(bc[i])
					print("bsearch",arr,bsearch(arr,x))
					num = num + bsearch(arr, x)
					print("num_a", num)
			print("1 turn")
			print("条件", num, q[2])
			if q[2] <= num:
				ub = x
			else:
				lb = x
		return lb, ub


print(solve())