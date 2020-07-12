max_v = 100

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
	# print("aa")
	global used
	while(True):
		used = [False for i in range(max_v)]
		f = dfs(s,t,float("inf"))
		if f == 0:
			return flow
		flow += f


n = 3
k = 3
can = [[False for i in range(n)]for j in range(k)]
can[0][0] = True
can[0][1] = True
can[1][0] = True
can[1][2] = True
can[2][1] = True

def solve():
	s = n + k
	t = s + 1

	for i in range(n):
		add_edge(s,i,1)
	for i in range(k):
		add_edge(n+i,t,1)
	for i in range(n):
		for j in range(k):
			if can[i][j]:
				add_edge(i, n+j, 1)

	print(max_flow(s,t))

solve()