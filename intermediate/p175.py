n = 2
m = 4
a = 2
b = 1
t =[3,1]

graph = [[2,3],[2,3],[0,1],[0,1]]

d = [[float("inf") for i in range(m)] for j in range(m)]

d[0][2] = 3
d[0][3] = 2
d[1][2] = 3
d[1][3] = 5
d[2][0] = 3
d[2][1] = 3
d[3][0] = 2
d[3][1] = 5

def solve():
	max_s = 1<<n
	print(max_s)
	dp = [[float("inf")for i in range(m)]for j in range(max_s)]
	dp[max_s-1][a-1] = 0
	for s in range(max_s-1, -1, -1):
		for v in range(m):
			for u in range(m):
				for k in range(n):
					if (s >> k & 1):
						dp[s&~(1<<k)][v] = min(dp[s&~(1<<k)][v], dp[s][u]+d[u][v]/t[k])
	print(dp)

solve()