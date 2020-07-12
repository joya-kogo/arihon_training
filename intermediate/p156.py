import math
np = 3
max_n = 20
c = 3
l = [5,5,5]
s = [1,2]
a = [270, 90]

seg_x = [0]*max_n
seg_y = [0]*max_n
seg_a = [180]*max_n
n = 1

def init(length):
	# 添字をうまく振れないので再帰で初期化
	# dpでも初期化可能かも
	global n
	count = 0
	while n < length:
		count = count + 1
		n *= 2
	k = 0
	for i in range(count):
		k = k * 2 + 1
	for i in range(k, k+np):
		# 葉を埋める
		seg_x[i] = 0
		seg_y[i] = l[i-k]
	for i in range(k-1, -1, -1):
		# それ以外を埋める
		seg_x[i] = 0
		seg_y[i] = seg_y[i*2+1] + seg_y[i*2+2]

def update(p, a, v, l, r):
	# print("start", p,l,r)
	if p <= l: 
		return
	elif p <= r:
		cl = v*2 + 1
		cr = v*2 + 2
		m = int((l + r)/2)
		# print("m", m)
		# print(l, m, r)
		if l <= p and p <= r:
			# print("angle change")
			seg_a[v] += a
			# print(v, seg_a[v])
		update(p,a,cl,l,m)
		update(p,a,cr,m+1,r)
		c = math.cos(math.radians(seg_a[v]-180))
		if abs(c) <= 0.0001:
			c = 0.0
		s = math.sin(math.radians(seg_a[v]-180))
		if abs(s) <= 0.0001:
			s = 0.0
		# print("cossin", v, seg_a[v]-180, c, s)
		seg_x[v] = seg_x[cl] + (c*seg_x[cr]-s*seg_y[cr])
		seg_y[v] = seg_y[cl] + (s*seg_x[cr]+c*seg_y[cr])
		# print("ataai", v, seg_x[v], seg_y[v])

def solve():
	init(np)
	# print(seg_x)
	# print(seg_y)
	# print(seg_a)
	for i in range(len(s)):
		# npだとバグる
		update(s[i],a[i]-180,0,0,np-1)
		print(seg_x[0],seg_y[0])
# init(np)
# print(seg_x)
# print(seg_y)
# print(seg_a)
# update(1, 90, 0, 0, np)
# update(2, -90, 0, 0, np)
solve()
# print(seg_x)
# print(seg_y)
# print(seg_a)