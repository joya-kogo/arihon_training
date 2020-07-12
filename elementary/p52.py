n = 4
item = [[2,3],[1,2],[3,4],[2,2]]
w = 5
v = []
naps = []
memo = [[0 for j in range(w+1)] for i in range(n+1)]
# x = [[foo for i in range(10)] for j in range(10)]
# print(x)
# 全探索(この書き方はくそ flagの情報は必要ない)
# valueの情報も情報もdpでは引数としては扱わない
# def add_or_not(flag, idx, capacity, value, nap):
# 	if idx == 4:
# 		v.append(value)
# 		print(nap)
# 		naps.append(nap)
# 		return
# 	if flag == 1 and item[idx][0] <= capacity:
# 		nap.append(item[idx])
# 		capacity = capacity - item[idx][0]
# 		value = value + item[idx][1]
# 	add_or_not(1, idx+1, capacity, value, nap)
# 	add_or_not(0, idx+1, capacity, value, nap)

# add_or_not(1, 0, w, 0, [])
# add_or_not(0, 0, w, 0, [])
# print(v)
# print(naps)

#引数、戻り値を出来るだけクリティカルなものにする
def search(idx, capacity):
	if 0 < memo[idx][capacity]:
		return memo[idx][capacity]
	res = 0
	if idx == 4:
		res = 0
	elif capacity < item[idx][0]:
		res = search(idx+1, capacity)
	else:
		res = max(search(idx+1, capacity), search(idx+1, capacity - item[idx][0])+item[idx][1])
	memo[idx][capacity] = res
	return res

# pure dp
# def dp():
# 	for i in range(n-1,-1,-1):
# 		print(i)
# 		for j in range(w+1):
# 			if j < item[i][0]:
# 				memo[i][j] = memo[i+1][j]
# 			else:
# 				# print(memo)
# 				memo[i][j] = max(memo[i+1][j], memo[i+1][j-item[i][0]]+item[i][1])
# 				# print(memo)

# dp()
print(search(0, w))