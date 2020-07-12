import numpy as np
import math
n = 8
xy = [[0,5],[1,8],[3,4],[6,2],[5,0],[6,6],[8,3],[8,7]]

class Point(object):
	"""docstring for Point"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

def minus(p1, p2):
	return p2.x - p1.x, p2.y - p1.y

def det(v1, v2):
	return v1[0]*v2[1] - v1[1]*v2[0]

def dist(p1, p2):
	return (p1.x - p2.x)**2 + (p1.y - p2.y)**2


# ちょっと冗長かも
def solve():
	global xy
	xy = sorted(xy)
	print(xy)
	ps = []
	conv_down = []
	for i in range(n):
		p = Point(xy[i][0],xy[i][1])
		ps.append(p)
	now_idx = -1

	for i in range(n-1):
		if i <= 1:
			conv_down.append(ps[i])
			now_idx += 1
		else:
			v1 = minus(conv_down[now_idx], conv_down[now_idx-1])
			v2 = minus(ps[i+1], conv_down[now_idx])
			dt = det(v1, v2)
			while 1 <= now_idx and dt <= 0:
				conv_down.remove(conv_down[now_idx])
				now_idx -= 1
				v1 = minus(conv_down[now_idx], conv_down[now_idx-1])
				v2 = minus(ps[i+1], conv_down[now_idx])
				dt = det(v1, v2)
			conv_down.append(ps[i+1])
			now_idx += 1
	conv_up = []
	now_idx = -1
	for i in range(n-1, 0, -1):
		if n-2 <= i:
			conv_up.append(ps[i])
			now_idx += 1
		else:
			v1 = minus(conv_up[now_idx], conv_up[now_idx-1])
			v2 = minus(ps[i-1], conv_up[now_idx])
			dt = det(v1, v2)
			while 1 <= now_idx and dt <= 0:
				conv_up.remove(conv_up[now_idx])
				now_idx -= 1
				v1 = minus(conv_up[now_idx], conv_up[now_idx-1])
				v2 = minus(ps[i-1], conv_up[now_idx])
				dt = det(v1, v2)
			conv_up.append(ps[i-1])
			now_idx += 1
	conv_up.extend(conv_down)
	convex = list(set(conv_up))
	res = 0
	for i in range(len(convex)):
		for j in range(len(convex)):
			res = max(res, dist(convex[i], convex[j]))
	print(res)


solve()