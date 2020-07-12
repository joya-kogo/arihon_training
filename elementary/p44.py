n = int(input())
s = [1,2,4,6,8]
t = [3,5,7,9,10]
now = 0
count = 0

for i in range(n):
	m = 100000
	midx = 100000
	for j in range(i,n):
		if now < s[j] and t[j] < m:
			m = t[j]
			midx = j
	if m != 100000 and midx != 100000:
		now = t[midx]
		count = count + 1
print(count)