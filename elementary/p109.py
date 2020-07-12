a = 11
b = 4
x = 0
y = 0


def gcd(a,b):
	d = a
	global x
	global y

	# 一つ下の階層の解x',y'を使って、現在の解x,yを計算できる
	# x = 1, y = 0
	if b!=0:
		d = gcd(b,a%b)
		temp = x
		x = y
		y = temp - ((a // b) * x)
	else:
		# a*x+0*y = gcd(a,0) = a
		# x = 1
		x = 1
		y = 0
	return d

ans = gcd(a,b)
print(a,b,x,y,ans)