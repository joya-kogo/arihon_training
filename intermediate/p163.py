import math

max_n = 20
seg = [0] * max_n
seg_q2 = [0] * max_n
n = 8

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
		seg[k] = seg[2*k+1]+seg[2*k+2]

def v_sum(a, b, k, l, r):
	if r < a or b < l:
		# r < a: 区間lrが区間abの左側　重ならない
		# b < l: 区間lrが区間abの右側　重ならない
		return 0
	if a <= l and r <= b:
		# 区間lrが区間abに含まれている
		return seg[k]
	else:
		vl = v_sum(a,b,k*2+1,l,math.floor((l+r)/2))
		vr = v_sum(a,b,k*2+2,math.floor((l+r)/2)+1,r)
		return vl + vr + seg_q2[k]

def h_sum(a,b,k,l,r,x):
	if r < a or b < l:
		return
	if (l<=a and b<=math.floor((l+r)/2)) or (math.floor((l+r)/2)+1<=a and b<=r):
		h_sum(a,b,k*2+1,l,math.floor((l+r)/2),x)
		h_sum(a,b,k*2+2,math.floor((l+r)/2)+1,r,x)
	else:
		seg_q2[k] = x


init(n)
update(0, 5)
update(1, 3)
update(2, 7)
update(3, 9)
update(4, 6)
update(5, 4)
update(6, 1)
update(7, 2)
print(seg)
print(h_sum(0,4,0,0,n-1,1*(4-0+1)))
print(seg_q2)
print(v_sum(0,6,0,0,n-1))
print(seg)