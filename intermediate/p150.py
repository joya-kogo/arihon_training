import queue

w = 10
h = 10
n = 5

x1 = [1,1,4,9,10]
x2 = [6,10,4,9,10]
y1 = [4,8,1,1,6]
y2 = [4,8,10,5,10]

def compress():
	newx = []
	newy = []
	for i in range(n):
		newx.append(x1[i])
		newx.append(x2[i])
		newy.append(y1[i])
		newy.append(y2[i])
		newx.append(x2[i] + 1)
		newy.append(y1[i] + 1)
	xs = list(set(sorted(newx)))
	ys = list(set(sorted(newy)))
	cx1 = bsearch(xs, x1)
	cx2 = bsearch(xs, x2)
	cy1 = bsearch(ys, y1)
	cy2 = bsearch(ys, y2)
	return cx1, cx2, cy1, cy2

def bsearch(sortx, x):
	ans = []
	for i in range(len(x)):
		ub = len(sortx)
		lb = -1
		while ub - lb > 1:
			mid = int((ub+lb)/2)
			if x[i] <= sortx[mid]:
				ub = mid
			else:
				lb = mid
		ans.append(ub)
	return ans

def solve():
	count = 0
	cx1, cx2, cy1, cy2 = compress()
	# 無駄ありそう?
	w = max(max(cx1), max(cx2)) + 1
	h = max(max(cy1), max(cy2)) + 1
	bd = [[0 for j in range(w)] for i in range(h)]
	for i in range(len(cx1)):
		for j in range(cx1[i], cx2[i]+1):
			for k in range(cy1[i], cy2[i]+1):
				bd[k][j] = 1
	for i in range(w):
		for j in range(h):
			if bd[j][i] == 0:
				count = count + 1
				bfs(bd, i, j, w, h)
	return count


def bfs(bd, x, y, w, h):
	xq = queue.Queue()
	yq = queue.Queue()
	bd[y][x] = 1
	xq.put(x)
	yq.put(y)
	while not xq.empty():
		x = xq.get()
		y = yq.get()
		for i in range(-1,2):
			for j in range(-1, 2):
				if 0<=x + i and x + i <= w-1:
					if 0<=y + j and y + j <= h-1:
						if bd[y+j][x+i] == 0 and (i == 0 or j == 0):
							bd[y+j][x+i] = 1
							xq.put(x+i)
							yq.put(y+j)
print(solve())