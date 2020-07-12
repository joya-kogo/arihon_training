import heapq
n = 3
l = [8,5,8]
h = []


cost = 0

for i in range(len(l)):
	heapq.heappush(h, l[i])


for i in range(n):
	if len(h) == 1:
		break
	cost = cost + heapq.heappop(h) + heapq.heappop(h)
	heapq.heappush(h, cost)

print(cost)