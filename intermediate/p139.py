n = 7
s = "BBFBFBB"
di = []
turn = [0] * n
for i in s:
	if i == "B":
		di.append(1)
	else:
		di.append(0)


def calc(k):
	sm = 0
	res = 0
	for i in range(n-k+1):
		# 後ろを向いているかどうか判定
		if (di[i] + sm) % 2 != 0:
			# i~i+k-1を反転させたらturn[i] = 1
			turn[i] = 1
			# 反転回数追加
			res = res + 1
		# j=i+1-k+1 ~ iまでのturn[j]の和=j = i-k+1 ~ i-1 turn[j]+turn[i]-turn[i-k+1]
		sm = sm + turn[i]
		if 0 <= i - k + 1:
			sm = sm - turn[i-k+1]
	for i in range(n-k+1, n):
		if (di[i] + sm) % 2 != 0:
			return -1
		if (0 <= i-k+1):
			sm = sm - turn[i-k+1]
	return res

print(calc(3))