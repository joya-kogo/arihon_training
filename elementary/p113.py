import math
max_n = 1000000
a = 22801763489
b = 22801787297

is_prime = [True]*(int(math.sqrt(b))+1)
is_prime_a_b = [True]*(max_n+1)


def sieve(n):
	p = 0
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,n+1):
		if is_prime[i]:
			p = p+1
			for j in range(2*i,n+1,i):
				is_prime[j] = False
	return p

# 区間a, bの素数の数
def sieve_term(a, b):
	print(sieve(int(math.sqrt(b))))
	for i in range(2, int(math.sqrt(b))+1):
		if is_prime[i]:
			for j in range(int((a+i-1)/i)*i,b,i):
				is_prime_a_b[j-a] = False


print(sieve_term(a,b))
t =0
for i in range(a,b):
	if is_prime_a_b[i-a] is True:
		t = t + 1
print(t)