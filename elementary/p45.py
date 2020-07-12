n = int(input())
s = "ACDBCB"
t = []

for i in range(n):
	sd = s[::-1]
	print(s,sd)
	if s < sd:
		t.append(s[0])
		s = s[1:len(s)]
	else:
		t.append(sd[0])
		s = s[0:len(s)-1]
print(t)