n = 6
k = 7
info = [[1,101,1],
[2,1,2],
[2,2,3],
[2,3,3],
[1,1,3],
[2,3,1],
[1,5,5]]
par = [0]*n*3
rank = [0]*n*3

def init(n):
	for i in range(n):
		par[i] = i

def find(x):
	if par[x] == x:
		return x
	par[x] = find(par[x])
	return par[x]

def unite(x, y):
	x = find(x)
	y = find(y)
	if x == y:return

	if rank[x] < rank[y]:
		par[x] = y
	else:
		par[y] = x
		if rank[x] == rank[y]: rank[x] = rank[x]+1


def same(x, y):
	return find(x) == find(y)

init(n*3)
ans = 0
for i in info:
	if 100 < i[1] or 100 < i[2]:
		print(i)
		ans = ans + 1
		continue
	if i[0] == 1:
		if same(i[1]-1,i[2]-1+n) or same(i[1]-1, i[2]-1+2*n):
			print("1")
			print(i)
			ans = ans + 1
			continue
		unite(i[1]-1,i[2]-1)
		unite(i[1]-1+n,i[2]-1+n)
		unite(i[1]-1+2*n,i[2]-1+2*n)
	if i[0] == 2:
		if same(i[1]-1, i[2]-1) or same(i[1]-1,i[2]-1+2*n):
			print("2")
			print(i)
			ans = ans + 1
			continue
		unite(i[1]-1,i[2]-1+n)
		unite(i[1]-1+n, i[2]-1+2*n)
		unite(i[1]-1+2*n, i[2]-1)
print(ans)