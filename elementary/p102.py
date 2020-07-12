import heapq

class Edge(object):
	def __init__(self, to, cost):
		self.to = to
		self.cost = cost

edges = [[Edge(1,100)],
		 [Edge(0,100),Edge(3,200),Edge(2,250)],
		 [Edge(1,250),Edge(3,100)],
		 [Edge(1,200),Edge(2,100)]]

max_v = 4
max_e = 4
h = []
d = [[float("inf") for j in range(max_v)] for i in range(2)]
print(d)

# vへの2番目の最短路...uまでの2番目の最短路+cost(u,v) or u以外の頂点tまでの最短路+cost(t,u)
# 最短だけを考慮し考慮しキューに投入していたのを、二番目まで入れる
def dijkstra(s):
	d[0][s] = 0
	d[1][s] = 0
	heapq.heappush(h, [d[0][s],s])
	while(len(h) != 0):
		v1 = heapq.heappop(h)
		# 取り出した頂点への2番目に短い距離よりもキューから取り出した頂点への距離が大きいか判定
		# 2番目より大きければ考慮しない
		if d[1][v1[1]] < v1[0]:
			 continue
		# 取り出した頂点につながる辺についてfor
		for i in range(len(edges[v1[1]])):
			e = edges[v1[1]][i]
			# 取り出した頂点までの距離に辺のコストを足す=辺のto頂点までの距離
			dd = v1[0] + e.cost
			# 辺のto頂点までの距離が、to頂点までの最短距離より短いか判定
			# 短ければ二つの値を入れ替えて、新たな最短距離と頂点番号をキューに投入
			if d[0][e.to] > dd:
				temp = d[0][e.to]
				d[0][e.to] = dd
				dd = temp
				heapq.heappush(h, [d[0][e.to], e.to])
			# 入れ替えにより、上のifを通ったら現在考慮している距離は元々の1番目と2番目の間になる
			# なので上のifにpassすると下のifにもpass
			# 2番目の最短を上書きしてキューに投入
			if d[1][e.to] > dd and dd > d[0][e.to]:
				d[1][e.to] = dd
				heapq.heappush(h, [d[1][e.to], e.to])
dijkstra(0)
print(d)