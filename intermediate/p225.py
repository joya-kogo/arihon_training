class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

def ccw(p0, p1, p2):
	dx1 = p1.x - p0.x
	dy1 = p1.y - p0.y
	dx2 = p2.x - p0.x
	dy2 = p2.y - p0.y
	if (dx1*dy2 > dx2*dy1):
		return 1
	if (dx1*dy2 < dx2*dy1):
		return -1
	if ((dx1*dx2 < 0) or (dy1*dy2 < 0)):
		return -2
	if ((dx1*dx1+dy1*dy1) < (dx2*dx2+dy2*dy2)):
		return 2
	return 0

def cross(p1, p2, p3, p4):
	a = (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0)
	b = (ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0)
	return (a and b)


n = 4
p = [[0,4],[0,1],[1,2],[1,0]]
q = [[4,1],[2,3],[3,4],[2,1]]
m = 4
ab = [[1,2],[1,4],[2,3],[2,4]]

def solve():
	ps = []
	qs = []
	for i in range(len(p)):
		ps.append(Point(p[i][0],p[i][1]))
		qs.append(Point(q[i][0],q[i][1]))
	for i in range(m):
		id1 = ab[i][0]-1
		id2 = ab[i][1]-1
		print(cross(ps[id1],qs[id1],ps[id2],qs[id2]))

solve()

