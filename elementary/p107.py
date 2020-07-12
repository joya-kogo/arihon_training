p1 = [1,11]
p2 = [5,3]

def gcd(a,b):
	if a%b==0:
		return b
	else:
		gcd(b,a%b)

print(gcd(abs(p2[1]-p1[1]),abs(p2[0]-p1[0]))-1)
