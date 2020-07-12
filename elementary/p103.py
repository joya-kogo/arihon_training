import heapq

n = 5
m = 5
r = 8

xyd = [[4,3,6831],[1,3,4583],[0,0,6592],[0,1,3063],[3,3,4975],[1,3,2049],[4,2,2104],[2,2,781]]

# class Edge(object):
# 	def __init__(self, to, cost):
# 		self.to = to
# 		self.cost = cost

# edges = [[] for j in range(n+m)]

# for i in range(r):
# 	edges[xyd[i][0]].append(Edge(xyd[i][1]+n,xyd[i][2]))
# 	edges[xyd[i][1]+n].append(Edge(xyd[i][0],xyd[i][2]))
# print(edges)

# cost = [[float("inf") for j in range(n+m)] for i in range(n+m)]
# for i in range(n+m):
# 	for j in range(len(edges[i])):
# 		cost[i][edges[i][j].to] = edges[i][j].cost
# print(cost)

# used = [False]*(n+m)
# mincost = [float("inf")]*(n+m)

# def prim():
# 	# 木からiまでの最小の距離
# 	mincost[0] = 0
# 	res = 0
# 	# h = []
# 	# heapq.heappush(h, [0,0])
# 	while True:
# 		v = -1
# 		for u in range(n+m):
# 			if used[u] is not True and (v == -1 or mincost[u] < mincost[v]):v = u
# 		print(v)
# 		if v == -1: break
# 		used[v] = True
# 		res += mincost[v]

# 		for u in range(n+m):
# 			mincost[u] = min(mincost[u], cost[v][u])

# 	return res

# print(prim())

max_v = n+m
max_e = r*2

par = [0]*(n+m)
rank = [0]*(n+m)

def init(n):
	for i in range(n):
		par[i] = i

def find(x):
	if par[x] == x:
		return x
	par[x] = find(par[x])
	return par[x]

def unite(x, y):
	x = find(x)
	y = find(y)
	if x == y:return

	if rank[x] < rank[y]:
		par[x] = y
	else:
		par[y] = x
		if rank[x] == rank[y]: rank[x] = rank[x]+1


def same(x, y):
	return find(x) == find(y)

class Edge(object):
	def __init__(self, fr, to, cost):
		self.fr = fr
		self.to = to
		self.cost = cost

edges = [ Edge(l[0],l[1]+5,-l[2]) for l in xyd]

edges = sorted(edges, key=lambda u: u.cost)

def kruskal():
	init(max_v)
	res = 0
	for i in range(r):
		e = edges[i]
		print(e.fr, e.to, same(e.fr, e.to))
		if same(e.fr, e.to) is not True:
			unite(e.fr, e.to)
			res = res + e.cost
	return res


print(10000*(n+m)+kruskal())

print(par)
print(rank)
