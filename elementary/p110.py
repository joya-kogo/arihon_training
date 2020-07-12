import math

def is_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0:
			return False
	return True

mods = []

def divisor(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0:
			mods.append(i)
			if i != int(n/i):
				mods.append(int(n/i))


def prime_factor(n):
	factor = [0]*n
	for i in range(2, int(math.sqrt(n))+1):
		# 一つ目の約数が見つかったらループに入る
		while(n % i == 0):
			# 約数でnを割り続け、余りが0でなくなったら終了
			# 見つかった約数の個数がわかる
			factor[i] = factor[i] + 1
			n = n // i
	if n != 1:
		factor[n] = 1
	return factor

print(is_prime(100))
divisor(100)
print(mods)
print(prime_factor(100))