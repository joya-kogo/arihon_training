n = 3
max_v = 100
k = 4

class Edge(object):
	def __init__(self, to, cap, rev):
		self.to = to
		self.cap = cap
		self.rev = rev

g = [[]for i in range(max_v)]

def add_edge(fr, to, cap):
	# len(g.to)などで逆辺を管理できている理由
	# toから見た何番目の辺か、をrevとして保持しておく
	# g[e.to][e.rev]でg[e.to]のe.rev番目の辺として逆辺にアクセスできる
	g[fr].append(Edge(to, cap, len(g[to])))
	g[to].append(Edge(fr, 0, len(g[fr])-1))
	# グラフにはこの段階でcap0の逆辺も追加されている

# Edge(1,10,0),Edge(2,6,1),Edge(2,2,0),Edge(3,6,1),Edge(2,3,3),Edge(4,8,3),Edge(4,5,2)
r = [1,1,2,3]
c = [1,3,2,2]

used = [False for i in range(max_v)]


def dfs(v, t, f):
	if v == t:
		return f
	used[v] = True
	# ある頂点から生えている辺についてfor
	# ある頂点から流せるpathを1頂点ずつ見ていっている
	# ここで逆辺も見ている
	for i in range(len(g[v])):
		e = g[v][i]
		# 辺の行き先の頂点が使われておらず、まだ容量に余裕があるかどうか
		# 使用中になるのはfrom側の頂点
		if not used[e.to] and e.cap > 0:
			# 辺の行き先からゴールまでdfs fとして現在のfとcapの小さい方を使う
			d = dfs(e.to, t, min(f,e.cap))
			# tに流れ込む時のdが返ってくる
			# そこまでに通ったpathのcapが変化
			if d > 0:
				e.cap -= d
				g[e.to][e.rev].cap += d
				return d
	# 流せるpathがなくなったら0が返る
	return 0

def max_flow(s,t):
	flow = 0
	global used
	while(True):
		used = [False for i in range(max_v)]
		f = dfs(s,t,float("inf"))
		if f == 0:
			print(flow)
			return flow
		flow += f

def solve():
	for i in range(k):
		print(r[i]-1, c[i]-1+n)
		add_edge(r[i]-1, c[i]-1+n, 1)
	for i in range(n):
		print(6, i)
		add_edge(6, i, 1)
	for i in range(n):
		print(i+n, 7)
		add_edge(i+n, 7, 1)
	print(max_flow(6, 7))

solve()