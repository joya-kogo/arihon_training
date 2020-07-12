p = 20
q = 3
a = [3,6,14]
dd = 0
gold = 0
for i in range(q):
	pmid = int((p-1)/2)
	m = float("inf")
	idx = -1
	for j in range(len(a)):
		if pmid-(a[j]-1) < m:
			m = abs(pmid-(a[j]-1))
			idx = j
			dd = j

def prison(now_p, now_a):
	if len(now_a) == 0:
		return 0
	pmid = int((now_p-1)/2)
	m = float("inf")
	idx = -1
	for j in range(len(now_a)):
		if pmid-(now_a[j]-1) < m:
			m = abs(pmid-(now_a[j]-1))
			idx = j
	res = now_p - 1
	head = now_a[idx]-1
	tail = now_p-now_a[idx]
	head_a = now_a[0:idx]
	tail_a = now_a[idx+1:len(now_a)]
	res = now_p - 1 + prison(head, head_a) + prison(tail, tail_a)
	return res

a = sorted(a)
print(prison(p,a))