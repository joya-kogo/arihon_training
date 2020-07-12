n = int(input())
num = []
for i in range(n):
	num.append(int(input()))
k = int(input())

idx = 0

def add_or_not(num, flag, idx, total):
	if idx == n:
		print(total)
		if total == k:
			print("Yes")
		return
	if flag == 1:
		total = total + num[idx]
		add_or_not(num, 1, idx+1, total)
		add_or_not(num, 0, idx+1, total)
	else:
		add_or_not(num, 1, idx+1, total)
		add_or_not(num, 0, idx+1, total)

add_or_not(num, 1, 0, 0)
add_or_not(num, 0, 0, 0)