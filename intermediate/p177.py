n = 3
m = 3
tile = [[".",".","."],[".","#","."],[".",".","."]]

# 北大の解説参照
# dp[i][j+1][s]を作るのにdp[i][j][s]しか使わない→さらにメモリ削減可能
# i = 2 j = 1のタイミングで答えの2になる
def solve():
	dp = [[[0 for i in range(1<<m)] for j in range(m+1)] for k in range(n+1)]
	dp[0][0][0] = 1
	for i in range(n):
		for j in range(m):
			for s in range(1<<m):
				# if i == 2 and j == 1 and s == 6:
				# print(i,j,s)
				# print(dp)
				if tile[i][j] == "#" or (s>>j&1):
					nx = s&~(1<<j)
					if j + 1 < m:
						dp[i][j+1][nx] += dp[i][j][s]
						# print("a",i, j+1, nx)
						# if i == 2 and j+1 == 2 and nx == 4:
						# 	print("111",i,j,s,dp[i][j][s])
						# 	print("111",i,j+1,nx,dp[i][j+1][nx])
					else:
						dp[i+1][0][nx] += dp[i][j][s]
						# print("b",i, j+1, nx)
						# if i == 2 and j+1 == 2 and nx == 4:
						# 	print("222",i,j,s,nx,dp[i][j][s])
				else:
					# 縦置き
					if i + 1 < n and tile[i+1][j] != "#":
						nx = s|(1<<j)
						if j + 1 < m:
							dp[i][j+1][nx] += dp[i][j][s]
							# print("c",i, j+1, nx)
							# if i == 2 and j+1 == 2 and nx == 4:
							# 	print("333",i,j,s,nx,dp[i][j][s])
						else:
							dp[i+1][0][nx] += dp[i][j][s]
							# print("d",i, j+1, nx)
							# if i == 2 and j+1 == 2 and nx == 4:
							# 	print("444",i,j,s,nx,dp[i][j][s])
					# 横置き
					if j + 1 < m and tile[i][j+1] != "#" and not s >> j+1 & 1:
						nx = s|(1<<(j+1))
						dp[i][j+1][nx] += dp[i][j][s]
						# print("e",i, j+1, nx)
						# if i == 2 and j+1 == 2 and nx == 4:
						# 	print("555",i,j,s,dp[i][j][s])
						# 	print("555",i,j+1,nx,dp[i][j+1][nx])
	print(dp[n-1][m-1][1<<m-1])


solve()