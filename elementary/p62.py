n = 3
a = [3,5,8]
m = [3,2,2]
t = 8
dp = [[-1 for j in range(t+1)] for i in range(n+1)]
for i in range(1, n+1):
	dp[i][0] = m[i-1]
print(dp)

# 自分で解いたもの
# for i in range(1,n+1):
# 	for j in range(1, t+1):
# 		if j - min(a) < 0:
# 			dp[i][j] = 0
# 		else:
# 			print(i,j)
# 			print(dp[i][j - a[i-1]] == 1)
# 			print(dp[i-1][j] == 1)
# 			print(j, a[i-1], m[i-1], int(j/a[i-1]) <= m[i-1])
# 			# 3つ目の条件がi-1番目の要素だけで考えているので間違い
# 			# dp[i][j]とdp[i+1][j]の関わり方が薄い→一つ前でjを作れていればok、というだけの関係よりも深いはず
# 			# dp[i+1][j]は、dp[i][j-k*a[i+1]]が作れているかによって決まる
# 			# すなわち、i番目まででjからi+1番目の数の倍数を引いた数を作れているかで決まる
# 			# もう一つループが必要
# 			if (dp[i][j - a[i-1]] == 1 or dp[i-1][j] == 1) and int(j/a[i-1]) <= m[i-1]:
# 				dp[i][j] = 1
# 				# print(dp)
# 			else:
# 				dp[i][j] = 0

# print(dp)


for i in range(1, n+1):
	for j in range(1,t+1):
		print(i, j, m[i-1], a[i-1])
		if 0 <= dp[i-1][j]:
			print("a")
			dp[i][j] = m[i-1]
		elif j < a[i-1] or dp[i][j-a[i-1]]< 0:
			print("b")
			dp[i][j] = -1
		else:
			print("c")
			dp[i][j] = dp[i][j-a[i-1]]-1
print(dp)