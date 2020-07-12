n = 6
r = 10
x = [1,7,15,20,30,50]
marked = []
count = 0


i = 0

# 非効率な実装
# while(i < n-1):
# 	# 黒く塗る点を探す
# 	pivot = x[i]+r
# 	print("pivot", pivot)
# 	idx = i
# 	for j in range(i,n):
# 		if x[j] <= pivot:
# 			idx = j
# 	if idx == i:
# 		# 現在位置からr以内に次の点がない場合
# 		idx = i + 1
# 	marked.append(x[idx])
# 	# 次の点を探す
# 	pivot = x[idx]+r
# 	for j in range(idx, n):
# 		if x[j] <= pivot:
# 			i = j

while(i < n):
	s = x[i]
	while(i < n and x[i] < s+r):
		i = i + 1
	p = x[i-1]
	marked.append(p)
	while(i < n and x[i] <= p+r):
		i = i + 1
print(marked)