import copy
m = 3
p = 0.75
x = 600000




# print(dp)

# m = 2、p = 0.5の条件で1回目でdp[2] = 0.5だけではいけない理由は、次のdp[2]が0になってしまうから
def solve():
	dp = [0] * (2**m+1)
	before = [0] * (2**m+1)
	key = int(1000000/(2**m))
	print(key)
	before[2**m] = 1
	dp[2**m] = 1
	# mステップに対するfor
	for i in range(m):
		# 2^mまでの範囲でfor
		for j in range(0,2**m):
			# jub...今j円持っている時に賭けられる額の最大値
			jub = min(j, 2**m-j)
			t = 0.0
			# かけられる額を1000000/2^m刻みで試す
			for k in range(0, jub+1):
				# 確率が最も高いものを記憶
				# 負けてj-k円になる確率1-p*j-k円で100000以上になる確率
				# 買ってj+K円になる確率p*j+K円で100000以上になる確率
				t = max(t, p*before[j+k]+(1-p)*before[j-k])
			dp[j] = t
		temp = before
		before = dp
		dp = temp
		# 最後の一回も逆転する
		print(before)
solve()


	# for i in range(m):
	# 	print("i", i)
	# 	d = int(1000000/int(1000000/(2**(i+1))))
	# 	d = int(2**m/d)
	# 	print("d", d)
	# 	before = copy.deepcopy(dp)
	# 	for j in range(0,2**m+1):
	# 			if j != 0 and j != 2**m:
	# 				print(j)
	# 				if -1 < j - d and j + d < 2**m+1:
	# 					print(i,j,before[j-d],before[j+d])
	# 					dp[j] = (1-p)*before[j-d]+p*before[j+d]
	# 					print(dp[j])
	# 			else:
	# 				if dp[j] == 0:
	# 					dp[j] = dp[j-1]
	# 	print(dp)