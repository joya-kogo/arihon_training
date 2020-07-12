import math

nn = 40
m = 6
st = [[20,30],[1,10],[10,20],[20,30],[15,25],[30,40]]

dp = [float("inf") for i in range(nn+1)]

seg = [0] * 128
n = 1

def init(length):
	global n
	while n < length:
		n *= 2
	print(n)
	for i in range(2*n-1):
		seg[i] = float("inf")

def update(k, a):
	# print("n",n)
	k += n-1
	seg[k] = a
	while k > 0 :
		k = math.floor((k-1)/2)
		seg[k] = min(seg[2*k+1],seg[2*k+2])

def query(a, b, k, l, r):
	if r < a or b < l:
		# r < a: 区間lrが区間abの左側　重ならない
		# b < l: 区間lrが区間abの右側　重ならない
		return float("inf")
	if a <= l and r <= b:
		# 区間lrが区間abに含まれている
		return seg[k]
	else:
		vl = query(a,b,k*2+1,l,math.floor((l+r)/2))
		vr = query(a,b,k*2+2,math.floor((l+r)/2)+1,r)
		return min(vl, vr)

def solve():
	init(nn)
	dp[1] = 0
	update(1,0)
	for i in range(m):
		v = min(dp[st[i][1]], query(st[i][0],st[i][1]+1,0,0,n-1)+1)
		dp[st[i][1]] = v
		update(st[i][1], v)
	print(dp[nn])

solve()