import math

n = 2
h = 10
r = 10
T = 100

g = 10.0

# k = 0
def height(T):
		# r...単位が㎝
		t = math.sqrt(2*h/g)
		print(t)
		k = math.floor(T/t)
		y = 0
		if k % 2 == 0:
			y = h - 1/2 * g * (T - k * t)**2
		else:
			y = h - 1/2 * g * (t + k * t - T)**2
		return y

yans = [0] * n
for i in range(n):
	yans[i] = height(T-i)
sorted(yans)
for i in range(n):
	ext = 2 * r * i / 100
	yans[i] = yans[i] + ext

print(yans)