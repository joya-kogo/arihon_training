n = 3
m = 4
z = [[100,100,100,1],[99,99,99,1],[98,98,98,1]]

import heapq

v = 30

class Edge(object):
	def __init__(self, to, cap, cost, rev):
		self.to = to
		self.cap = cap
		self.cost = cost
		self.rev = rev

g = [[]for i in range(v)]
prev_v = [100 for i in range(v)]
prev_e = [100 for i in range(v)]

def add_edge(fr, to, cost, cap):
	# len(g.to)などで逆辺を管理できている理由
	# toから見た何番目の辺か、をrevとして保持しておく
	# g[e.to][e.rev]でg[e.to]のe.rev番目の辺として逆辺にアクセスできる
	g[fr].append(Edge(to, cap, cost, len(g[to])))
	g[to].append(Edge(fr, 0, -cost, len(g[fr])-1))
	# グラフにはこの段階でcap0の逆辺も追加されている

d = [float("inf") for i in range(v)]
h = [0 for i in range(v)]

def min_cost_flow(s, t, f):
	global d
	global v
	global h
	res = 0
	d = [float("inf") for i in range(v)]
	while(f>0):
		q = []
		for i in range(v):
			d[i] = float("inf")
		d[s] = 0
		heapq.heappush(q, [0,s])
		while len(q) != 0:
			p = heapq.heappop(q)
			vidx = p[1]
			if d[vidx] < p[0]:
				continue
			for j in range(len(g[vidx])):
				e = g[vidx][j]
				if e.cap > 0 and d[e.to] > d[vidx]+e.cost+h[vidx]-h[e.to]:
					d[e.to] = d[vidx]+e.cost+h[vidx]-h[e.to]
					prev_v[e.to] = vidx
					prev_e[e.to] = j
					heapq.heappush(q, [d[e.to], e.to])
		if d[t] == float("inf"):
			return -1
		for i in range(v):
			h[i] += d[i]
		c = f
		vidx = t
		while True:
			if vidx == s:
				break
			c = min(c, g[prev_v[vidx]][prev_e[vidx]].cap)
			vidx = prev_v[vidx]
		f -= c
		res += c * h[t]
		vidx = t
		while True:
			if vidx == s:
				break
			e = g[prev_v[vidx]][prev_e[vidx]]
			e.cap -= c
			g[vidx][e.rev].cap += c
			vidx = prev_v[vidx]
	return res

def make_graph():
	s = n + n * m
	t = s + 1
	for j in range(m):
		for k in range(n):
			add_edge(n + j * n + k, t, 0, 1)
			for i in range(n):
				# おもちゃとマッチングさせるn倍までの工場を作る
				add_edge(i,n + j*n+k, (k+1)*z[i][j], 1)
	for i in range(n):
		add_edge(s, i, 0, 1)

def solve():
	make_graph()
	print(min_cost_flow(n + n * m, n + n * m+1, n))

solve()