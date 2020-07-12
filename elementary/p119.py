n = 3

matrix = [[0,0,1],[1,0,0],[0,1,0]]
rank = [-1]*n

for i in range(n):
	for j in range(n):
		if matrix[i][j] == 1:
			rank[i] = j

count = 0
for k in range(n):
	m = float("inf")
	idx = -1
	for i in range(k,n):
		if rank[i] < m:
			m = rank[i]
			idx = i
	for j in range(i,0,-1):
		if rank[j] < rank[j-1]:
			temp = rank[j]
			rank[j] = rank[j-1]
			rank[j-1] = temp
			count = count + 1
			tp = matrix[j]
			matrix[j] = matrix[j-1]
			matrix[j-1] = tp
	flag = True
	for l in range(n):
		if rank[l] > l:
			flag = False
	if flag is True:
		break
print(count)