import heapq

n = 4
l = 25
p = 10
a = [10,14,20,21]
b = [10, 5, 2, 4]

h = []
# for i, j in zip(a, b):
# 	heapq.heappush(h, (i, j))

# print(h)


# ガソリンがスタンドの合間で切れる可能性がある
# for i in range(1, len(a)):
# 	p = p + heapq.heappop(h)[1]
# 	if l <= p:
# 		print(i)
# 		break
pos  = 0
count = 0
while True:
	p = p - 1
	pos = pos + 1
	for i in range(0, len(a)):
		if pos == a[i]:
			heapq.heappush(h, (b[i], a[i]))
	if pos == l:
		print(count)
		break
	if p == 0:
		if len(h) == 0:
			print(-1)
			break
		p = p + heapq.heappop(h)[1]
		count = count + 1
