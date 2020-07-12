import math

def mod_pow(x,n,mod):
	res = 1
	while (n > 0):
		# print("n1")
		# print(n)
		# print(n&1)
		if n&1:
			# print("res")
			# print(res)
			res = res * x % mod
			# print(res)
		# print("x1")
		# print(x)
		x = x * x % mod
		# print(x)
		# print("n2")
		# print(n)
		n = n >> 1
		# print(n)
	return res

n = 8
print(mod_pow(13,n,n))
for i in range(2,n):
	print(i, mod_pow(i,n,n))
	# print(i, math.pow(i,17), math.pow(i,17)%17,i%17)

