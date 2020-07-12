n = 5
a = [4,2,3,1,5]

dp = [0]*n
dp[0] = 1

# O(n^2)
# 最初から表にしようとせず、前のものを使って次をどう表せるか考える
for i in range(1, n):
	m = 1
	for j in range(i-1,-1,-1):
		if a[j] < a[i]:
			if m < dp[j] + 1:
				m = dp[j] + 1
	dp[i] = m



print(dp)