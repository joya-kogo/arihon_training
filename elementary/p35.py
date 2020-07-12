n = int(input())
m = int(input())
l = []

lake = ["w........ww.",
		".www.....www",
		"....ww...ww.",
		".........ww.",
		".........w..",
		"..w......w..",
		".w.w.....ww.",
		"w.w.w.....w.",
		".w.w......w.",
		"..w.......w."]

def dfs(x,y):
	if lake[x][y] == ".":
		return
	if lake[x][y] == "w":
		tmp = list(lake[x])
		tmp[y] = "."
		lake[x] = "".join(tmp)
	if 0 <= x-1 and lake[x-1][y] == "w":
		dfs(x-1,y)
	if x+1 <= 9 and lake[x+1][y] == "w":
		dfs(x+1,y)
	if 0 <= y-1 and lake[x][y-1] == "w":
		dfs(x,y-1)
	if y+1 <= 11 and lake[x][y+1] == "w":
		dfs(x,y+1)
	if 0 <= x-1 and 0 <= y-1 and lake[x-1][y-1] == "w":
		dfs(x-1, y-1)
	if 0 <= x-1 and y+1 <= 11 and lake[x-1][y+1] == "w":
		dfs(x-1, y+1)
	if x+1 <= 9 and 0 <= y-1 and lake[x+1][y-1] == "w":
		dfs(x+1, y-1)
	if x+1 <= 9 and y+1 <= 11 and lake[x+1][y+1] == "w":
		dfs(x+1, y+1)

def search_w():
	for i in range(n):
		for j in range(m):
			if lake[i][j] == "w":
				return i, j

def is_end():
	for i in range(n):
		for j in range(m):
			if lake[i][j] == "w":
				return False
	return True

count = 0
while(True):
	i, j = search_w()
	dfs(i,j)
	count = count + 1
	if is_end():
		break
print(count)