n = 10
s = 15
a = [5,1,3,5,10,7,4,9,2,8]

n_sum = []
now = 0
for num in a:
	now = now + num
	n_sum.append(now)
print(n_sum)

# しゃくとり法ではないバージョン
def solve():
	start = 0
	min_start = 0
	m = float("inf")
	while(n_sum[start]+s<=n_sum[n-1]):
		ub = n
		lb = start
		while ub - lb > 1:
			mid = int((ub+lb)/2)
			if s<=n_sum[mid]-n_sum[start]:
				ub = mid
			else:
				lb = mid
		if ub < m:
			m = ub
			min_start = lb
		start = start + 1
	return min_start, m


def scale_insect():
	start = 0
	end = 0
	sm = 0
	res = float("inf")
	while True:
		while end < n and sm < s:
			sm = sm + a[end]
			end = end + 1
		if sm < s:
			break
		res = min(res, end-start)
		start = start + 1
		sm = sm - a[start]
	return res

		# クソ実装
		# while True:
		# 	if n-1 < end:
		# 		return res
		# 	sm = sm + a[end]
		# 	print("b", start, end, sm)
		# 	if s <= sm:
		# 		if end-start < res:
		# 			res = end-start
		# 		# start = start + 1
		# 		break
		# 	end = end + 1
		# while True:
		# 	sm = sm - a[start]
		# 	print("a",start,end, sm)
		# 	if sm < s:
		# 		end = end + 1
		# 		break
		# 	start = start + 1

print(scale_insect())