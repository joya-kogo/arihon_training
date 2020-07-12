max_n = 100000

prime = [-1]*max_n
is_prime = [True]*(max_n+1)


def sieve(n):
	p = 0
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,n+1):
		if is_prime[i]:
			p = p+1
			prime[p] = i
			for j in range(2*i,n+1,i):
				is_prime[j] = False
	return p

print(sieve(10))