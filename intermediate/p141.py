import copy

m = 4
n = 4

tile = [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]]

first = []

def dfs(s, flag):
	if flag:
		s.append(1)
	else:
		s.append(0)
	if len(s) == 4:
		first.append(s)
		return
	dfs(copy.deepcopy(s), True)
	dfs(copy.deepcopy(s), False)

dfs([],True)
dfs([],False)
print(first)

# 塗った場所

def solve():
	ans = [[0 for k in range(m)] for j in range(n)]
	best = [[0 for k in range(m)] for j in range(n)]
	for i in range(2**n):
		start = first[i]
		print(start)
		ans[0] = start
		now = copy.deepcopy(tile)
		for l in range(n):
			if start[l] == 1:
				now[0][l] = (start[l] + now[0][l])%2
				now[1][l] = (1 + now[1][l])%2
				if l != 0:
					now[0][l-1] = (1 + now[0][l-1])%2
				if l != n - 1:
					now[0][l+1] = (1 + now[0][l+1])%2
		# print("start", now)
		for j in range(1, n):
			# print(j)
			for k in range(n):
				if now[j-1][k] == 1:
					ans[j][k] = 1
					now[j][k] = (1 + now[j][k])%2
					if k != 0:
						now[j][k-1] = (1 + now[j][k-1])%2
					if k != n - 1:
						now[j][k+1] = (1 + now[j][k+1])%2
					if j != 0:
						now[j-1][k] = (1 + now[j-1][k])%2
					if j != m - 1:
						now[j+1][k] = (1 + now[j+1][k])%2
			# print(now)
			start = ans[j]
		flag = True
		for o in range(n):
			for p in range(m):
				if now[o][p] == 1:
					flag = False
		if flag is True:
			best = now
			return best
	return "impossible"

print(solve())