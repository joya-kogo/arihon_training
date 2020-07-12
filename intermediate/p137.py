import collections
import copy

p = 5
a = [1,8,8,8,1]

# sm = []
sm = {}

b = collections.Counter(a)
for i in range(p):
	if a[i] not in sm:
		sm[a[i]] = 0

# for i in range(p):
# 	now[a[i]] = now[a[i]] + 1
# 	sm.append(copy.deepcopy(now))
print(sm)

# def judge(x):
# 	if all(1<=value for value in x.values()):
# 		return True
# 	else:
# 		return False

# print(judge(sm[0]))

def solve():
	num = 0
	start = 0
	end = 0
	res = float("inf")
	# 出現回数1以上のものがいくつあったか覚えておく
	while True:
		while end < p and num < len(sm):
			if sm[a[end]] == 0:
				num = num + 1
			sm[a[end]] = sm[a[end]] + 1
			end = end + 1
		if num < len(sm):
			break
		res = min(res, end - start)
		sm[a[start]] = sm[a[start]] - 1
		if sm[a[start]] == 0:
			num = num - 1
		start = start + 1
	return res

print(solve())