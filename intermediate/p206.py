import queue

x = 5
y = 5
tile = [["X","X","D","X","X"],
		["X",".",".",".","X"],
		["D",".",".",".","X"],
		["X",".",".",".","D"],
		["X","X","X","X","X"]]


d = [[[[-1 for l in range(x)]for k in range(y)]for j in range(x)]for i in range(y)]


def bfs(i, j):
	global d
	si = i
	sj = j
	d[si][sj][i][j] = 0
	q = queue.Queue()
	q.put([i, j])
	while not q.empty():
		s = q.get()
		i = s[0]
		j = s[1]
		for dx in range(-1, 2):
			for dy in range(-1, 2):
				if abs(dx) != abs(dy) and 0<=i+dy and i+dy<=y-1 and 0<=j+dx and j+dx<=x-1:
					# if i+dy == 0 and j + dx == 2:
						# print(i, j, dy, dx,d[1][1])
					if tile[i+dy][j+dx] == "." and d[si][sj][i+dy][j+dx] == -1:
						d[si][sj][i+dy][j+dx] = d[si][sj][i][j] + 1
						q.put([i+dy, j+dx])
					elif tile[i+dy][j+dx] == "D" and d[si][sj][i+dy][j+dx] == -1:
						d[si][sj][i+dy][j+dx] = d[si][sj][i][j] + 1

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
	for i in range(len(g[v])):
		e = g[v][i]
		if not used[e.to] and e.cap > 0:
			dist = dfs(e.to, t, min(f,e.cap))
			if dist > 0:
				e.cap -= dist
				g[e.to][e.rev].cap += dist
				return dist
	return 0

def max_flow(s,t):
	flow = 0
	global used
	while(True):
		used = [False for i in range(max_v)]
		f = dfs(s,t,float("inf"))
		if f == 0:
			return flow
		flow += f

def make_graph(points, doors, t):
	# print(points)
	# print(doors)
	global g
	g = [[]for i in range(max_v)]
	k = t
	for i in range(len(points)):
		for j in range(len(doors)):
			# for k in range(1,t+1):
				# print(k)
			# print(points[i], doors[j], d[points[i][0]][points[i][1]][doors[j][0]][doors[j][1]])
			if d[points[i][0]][points[i][1]][doors[j][0]][doors[j][1]] == k:
				# print("Yes", i, len(points)+len(doors)*(k-1)+j)
				# print("Yes",points[i], doors[j], k)
				# print("edge",i, len(points)+len(doors)*(k-1)+j)
				add_edge(i, len(points)+len(doors)*(k-1)+j, 1)

	# startとendにたす
	for i in range(len(points)):
		# print(len(points)+t*len(doors), i)
		add_edge(len(points)+t*len(doors), i, 1)
	for i in range(len(doors)):
		for j in range(1,t+1):
			# print(i+len(doors)*(k-1)+len(points), len(points)+t*len(doors)+1)
			add_edge(i+len(doors)*(j-1)+len(points), len(points)+t*len(doors)+1, 1)
	return max_flow(len(points)+t*len(doors), len(points)+t*len(doors)+1)

def solve():
	points = []
	doors = []
	for i in range(x):
		for j in range(y):
			if tile[i][j] == ".":
				bfs(i, j)
				points.append([i, j])
			elif tile[i][j] == "D":
				doors.append([i, j])
	res = 0
	t = 1
	# グラフリセットが必要?→要考察
	while True:
		res += make_graph(points, doors, t)
		if res == len(points):
			return t
		t = t + 1



print(solve())