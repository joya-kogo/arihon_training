n = 5
a = [2,3,3,5,6]
k = 3

def lower_bound():
	lb = -1
	ub = n
	while (ub-lb > 1):
		mid = int((ub+lb)/2)
		print(mid, lb, ub)
		if k <= a[mid]:
			# 今のa[mid]が条件を満たしていたら、解は左側にある
			ub = mid
		else:
			# 今のa[mid]が条件を満たしていなければ、解は右側にある
			lb = mid
	return ub

print(lower_bound())