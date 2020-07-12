n = 6
a = [-45,-41,-36,-36,-26,-32]
b = [22,-27,53,30,-38,-54]
c = [42,56,-37,-75,-10,-6]
d = [-16,30,77,-46,62,45]

ab = []
cd = []

for i in range(n):
	for j in range(n):
		ab.append(a[i]+b[j])
		cd.append(c[i]+d[j])


cd = sorted(cd)
res = 0
for i in range(n**2):
	key = 0 - ab[i]
	lb = -1
	ub = n ** 2
	while(ub - lb > 1):
		mid = int((lb+ub)/2)
		if key <= cd[mid]:
			ub = mid
		else:
			lb = mid
	if (key == cd[ub]):
		res = res + 1
print(res)