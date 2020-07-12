n = 3
item = [[3,4],[4,5],[2,3]]
w = 7
dp = [[0 for j in range(w+1)] for i in range(n+1)]

def search(i, j):
	if 0 < dp[i][j]:
		return dp[i][j]
	res = 0
	if i == n:
		res = 0
	elif j < item[i][0]:
		res = search(i+1, j)
	else:
		# ダメな理由:入れないで次の荷物に行くか、入れて次の荷物に行くか、入れて今の荷物を再度検討するか選んでいる
		# dp[i][j]を表現する式にi, j自身が入っている→うまくdpで書けない？
		# 合ってそう
		res = max(search(i+1, j), search(i+1, j-item[i][0])+item[i][1], search(i, j-item[i][0])+item[i][1])
	dp[i][j] = res
	print(dp[i][j])
	return res

def dpme():
	for i in range(n-1, -1, -1):
		for j in range(w+1):
			if j < item[i][0]:
				dp[i][j] = dp[i+1][j]
			else:
				dp[i][j] = max(dp[i+1][j], dp[i+1][j-item[i][0]]+item[i][1], dp[i][j-item[i][0]]+item[i][1])

def dpans():
	# 複数回の使用を許して、i番目の品物までで重さjまでで最大の価値をメモ化している
	for i in range(n):
		for j in range(w+1):
			for k in range(n):
				if j < k * item[i][0]:
					# print("out")
					# print(i,j,k,dp[i+1][j], dp[i][j-k*item[i][0]]+k*item[i][1])
					break
				print("safe")
				print(dp)
				print(i,j,k,dp[i+1][j], dp[i][j-k*item[i][0]]+k*item[i][1])
				dp[i+1][j] = max(dp[i+1][j], dp[i][j-k*item[i][0]]+k*item[i][1])





print(dpans())
print(dp)