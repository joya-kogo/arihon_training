import math
n = 1
v = 7
xy = [3,1]
lbrt = [[1,1,2,2]]

g = 9.8

def solve():
	ok = True
	for i in lbrt:
		ok = judge(i[0],i[3]) and ok
		ok = judge(i[2],i[3]) and ok
	return ok

def calc_h(vy, t):
	return -1*g*(t**2)/2 + vy * t


def coll(lb, ub, value):
	if value <= ub and lb <= value:
		return False
	else:
		return True



def judge(qx, qy):
	a = 1/4*g**2
	b = g*qy-v**2
	c = qx**2+qy**2
	# print(a,b,c)
	for i in range(-1, 2, 2):
		print(i)
		t = (-b+i+math.sqrt(b**2-4*a*c))/2*a
		vx = qx/t
		vy = (qy-1*g*(t**2)/2)/t
		x = xy[0]
		y = xy[1]
		h = calc_h(vy, x/t)
		if h < y:
			continue
		flag = True
		for i in range(n):
			l = lbrt[i][0]
			b = lbrt[i][1]
			r = lbrt[i][2]
			t = labrt[i][3]
			if x<=l:
				continue
			if r == x and y <= t and b <= h:
				flag = False
			yl = coll(b,t,calc_h(vy, l/vx))
			yr = coll(b,t,calc_h(vy, r/vx))
			xh = coll(l,r,vx*(vy/g))
			yh = coll(b,t,calc_h(vy, vy/g))
			if not (yl and yr and xh and yh):
				flag = False
		if flag:
			return True
	return False




print(solve())