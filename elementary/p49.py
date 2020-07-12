n = 3
l = [8,5,8]

cost = sum(l)
print(cost)
l = sorted(l)
total = 0
count = 1

while(True):
	count = count + 1
	total = total + cost
	l1 = max(l)
	print(l1)
	l2 = cost - l1
	print(l2)
	l = l[1:len(l)]
	cost = l2
	if count == n:
		print(total)
		exit()
