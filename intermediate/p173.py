n = 5



class Edge(object):
	def __init__(self, fr, to, cost):
		self.fr = fr
		self.to = to
		self.cost = cost

# edge = [Edge(0,1,3),Edge(0,3,4),Edge(1,2,5),Edge(2,0,4),Edge(2,3,5),Edge(3,4,3),Edge(4,0,7),Edge(4,1,6)]
edge = [[1,3],[2],[0,3],[4],[0,1]]
d = [[ float("inf") for i in range(n)]for j in range(n)]
d[0][1] = 3
d[0][3] = 4
d[1][2] = 5
d[2][0] = 4
d[2][3] = 5
d[3][4] = 3
d[4][0] = 7
d[4][1] = 6
print(d)

def encoding(arr):
	b = 0
	for i in arr:
		b = b + 2**i
	return b

max_idx = encoding([0,1,2,3,4])
dp = [[-1 for j in range(n)]for i in range(max_idx+1)]

def solve(s,v):
	if 0<=dp[s][v]:
		print("aaa")
		return dp[s][v]
	if s == max_idx and v == 0:
		print("bbb")
		dp[s][v] = 0
		return 0
	r = float("inf")
	for u in range(n):
		if not (s >> u & 1):
			print(s, u)
			r = min(r, solve(s|1<<u, u)+ d[u][v])
	dp[s][v] = r
	return r


def bitdp():
	dp2 = [[float("inf") for j in range(n)]for i in range(max_idx+1)]
	dp2[(1<<n)-1][0] = 0
	for s in range((1<<n)-2, -1, -1):
		for v in range(n):
			for u in range(n):
				if not(s >> u & 1):
					dp2[s][v] = min(dp2[s][v], dp2[s|1<<u][u]+ d[u][v])
					print("ss", s, u, v, dp2[s][v])
	print(dp2)
	return dp2[0][0]

print(bitdp())
print(dp)