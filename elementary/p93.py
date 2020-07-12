G = []
n = int(input())
for i in range(n):
	s = input().split()
	G.append([])
	for j in range(len(s)):
		G[i].append(int(s[j]))

print(G)
color = [-1]*n

# O(|V||E|)?...非効率 1→2と2→1をどちらも探索している
def dfs(now, fr, start, col):
	if now == start and color[now] == -1:
		color[now] = col
	elif now == start and color[now] != col:
		print("No")
		return
	elif now == start and color[now] == col:
		print("Yes")
		return

	for i in G[now]:
		if fr != i:
			print(fr,now,i)
			if col == 1:
				dfs(i, now, start, 0)
			else:
				dfs(i, now, start, 1)



dfs(0,0,0,0)