n = 3
k = 1
abw = [[1,3,2],[2,3,4],[3,4,8]]

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

def min_cost_flow(s, t, f):
	global d
	global v
	res = 0
	d = [float("inf") for i in range(v)]
	while(f>0):
		for i in range(v):
			d[i] = float("inf")
		d[s] = 0
		update = True
		while update:
			update = False
			for i in range(v):
				if d[i] == float("inf"):
					continue
				for j in range(len(g[i])):
					e = g[i][j]
					if e.cap > 0 and d[e.to] > d[i]+e.cost:
						d[e.to] = d[i]+e.cost
						prev_v[e.to] = i
						prev_e[e.to] = j
						update = True
		if d[t] == float("inf"):
			return -1
		c = f
		vidx = t
		while True:
			if vidx == s:
				break
			c = min(c, g[prev_v[vidx]][prev_e[vidx]].cap)
			vidx = prev_v[vidx]
		f -= c
		res += c * d[t]
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
	su = []
	res = 0
	for i in range(n):
		su.append(abw[i][0])
		su.append(abw[i][1])
	su = sorted(su)
	su = list(set(su))
	m = len(su)
	s = m
	t = s + 1
	add_edge(s, 0, 0, k)
	add_edge(m-1, t, 0, k)
	for i in range(m-1):
		add_edge(i, i+1, 0, float("inf"))

	for i in range(n):
		u = su.index(abw[i][0])
		v = su.index(abw[i][1])
		add_edge(s, v, 0, 1)
		add_edge(u, t, 0, 1)
		add_edge(v, u, abw[i][2], 1)
		res -= abw[i][2]
	return m, res

def solve():
	ls, res = make_graph()
	print(res)
	res += min_cost_flow(ls, ls+1, k+n)
	print(-res)

solve()