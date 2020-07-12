n = 4
m = 4
s = "abcd"
t = "becd"

dp = [[0 for j in range(n+1)] for i in range(m+1)]

# for i in range(n):
# 	for j in range(m):
# 		if s[i] == t[j]:
# 			print(i, j)
# 			dp[i+1][j+1] = dp[i][j]+1
# 		else:
# 			dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])


def search(i, j):
	print(i, j)
	# メモ化されていればその値を呼ぶ
	if 0 < dp[j][i]:
		return dp[j][i]
	res = 0
	if i == n or j == m:
		# 端まで到達したらその時点での部分文字列の最長を返す
		return res
	if s[i] == t[j]:
		res = search(i+1,j+1)+ 1
	else:
		res = max(search(i+1, j), search(i, j+1))
	dp[i][j] = res
	return res

print(search(0,0))