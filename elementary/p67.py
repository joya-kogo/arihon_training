n = 3
m = 3
a = [1,2,3]
M = 10000

dp = [[0 for j in range(n+1)] for i in range(m+1)]
dp[0][0] = 1
dp[1][0] = 1
dp[2][0] = 1
dp[3][0] = 1

for i in range(n):
	for j in range(1, m+1):
		if 0<= j-1-a[i]:
			# i-1番目からj-k個選び、i番目でk個選ぶ
			# j-1の時を考えると、足りない項と余っている項が二つある
			# それらを足し/引きすることにより漸化式を作れる
			dp[i+1][j] = dp[i+1][j-1]+dp[i][j]-dp[i][j-1-a[i]]
		else:
			print(i, j, dp[i+1][j-1], dp[i][j])
			dp[i+1][j] = dp[i+1][j-1]+dp[i][j]

print(dp)