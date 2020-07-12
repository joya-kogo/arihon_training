n = 3

v1 = [1,3,-5]
v2 = [4,1,-2]

v1 = sorted(v1)
v2 = sorted(v2, reverse=True)

res = 0
for i in range(n):
	res = res + v1[i]*v2[i]

print(res)