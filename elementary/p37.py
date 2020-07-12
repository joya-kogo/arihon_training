meiro =["#s#######.#",
		"......#..#",
		".#.##.#.##",
		".#........",
		"##.##.####",
		"....#....#",
		".#######.#",
		"....#.....",
		".####.###.",
		"....#...G#"]

import queue

n = int(input())
m = int(input())
i = 1
j = 1
iqueue = queue.Queue()
jqueue = queue.Queue()
iqueue.put(i)
jqueue.put(j)
visited = [[0,2]]
distance = []
for i in range(10):
	distance.append([0]*10)
print(distance)
distance[i][j] = 1
print(distance)
count = 0
status = ""
while(not iqueue.empty() and status != "goal"):
	print(i,j)
	i = iqueue.get()
	j = jqueue.get()
	print(i,j)
	if meiro[i][j] == "G":
		print("Goal")
		status = "goal"
	visited.append([i,j])
	for k in range(-1,2):
		for l in range(-1,2):
			if k == 0 or l == 0:
				if k == 0 and l == 0:
					continue
				if 1<=i+k and i+k <= 9 and meiro[i+k][j] == "." and distance[i+k][j] == 0:
					iqueue.put(i+k)
					jqueue.put(j)
					distance[i+k][j] = distance[i][j] + 1
				if 1<=j+l and j+l <= 9 and meiro[i][j+l] == "." and distance[i][j+l] == 0:
					iqueue.put(i)
					jqueue.put(j+l)
					distance[i][j+l] = distance[i][j] + 1
print(distance[9][7])
