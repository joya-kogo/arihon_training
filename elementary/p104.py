n = 4
ML = 2
MD = 1
MLS = [[1,3,10],[2,4,20]]
MDS = [[2,3,3]]

class Edge(object):
	def __init__(self, fr, to, cost):
		self.fr = fr
		self.to = to
		self.cost = cost

edges = []
# d[1]+10 => d[3]

d  = [float("inf")]*n

for ml in MLS:
	e = Edge(ml[0]-1, ml[1]-1, ml[2])
	edges.append(e)

for md in MDS:
	e = Edge(md[1]-1, md[0]-1, -md[2])
	edges.append(e)

for i in range(1, n):
	e = Edge(i, i-1, 0)
	# if e.fr == 2:
	# 	continue
	edges.append(e)

print(edges)
e = len(edges)

def bellman_ford(s):
	d[s] = 0
	while True:
		update = False
		for i in range(e):
			edge = edges[i]
			print(edge.fr, edge.to, edge.cost, d[edge.fr] + edge.cost, d[edge.to])
			print(d)
			# if edge.cost == -3:
			# 	print("gg")
			if d[edge.fr] != float("inf") and d[edge.fr] + edge.cost < d[edge.to]:
				d[edge.to] = d[edge.fr] + edge.cost
				update = True
		if update is not True:
			break

bellman_ford(0)
print(d)

# 閉路検出&inf略
