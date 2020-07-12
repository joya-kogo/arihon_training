n = 4
item = [[2,3],[1,2],[3,4],[2,2]]
w = 5
dp = [[0 for j in range(7+1)] for i in range(n+1)]
dp[0] = [0]
for i in range(6+1):
	dp[0].append(float('inf'))

for i in range(0, 4):
	for j in range(1, 8):
		if j < item[i][1]:
			dp[i+1][j] = dp[i][j]
		else:
			dp[i+1][j] = min(dp[i][j], dp[i][j-item[i][1]]+item[i][0])

print(dp)