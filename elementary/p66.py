n = 4
m = 3
M = 10000

dp = [[0 for j in range(n+1)] for i in range(m+1)]
# for i in range(0, m+1):
# 	dp[i][0] = 1
# for j in range(0, n+1):
# 	dp[0][j] = 0
dp[0][0] = 1

# dp[i+1][j]=...だとバグる理由
for i in range(m+1):
	for j in range(n+1):
		print(i, j, j-i)
		# i-1個に分ける方法+丁度i個に分ける方法
		if 0<=j - i:
			dp[i][j] = dp[i-1][j] + dp[i][j-i]
		else:
			dp[i][j] = dp[i-1][j]

print(dp)