k1 = int(input())
k5 = int(input())
k10 = int(input())
k50 = int(input())
k100 = int(input())
k500 = int(input())
num = [k500,k100,k50,k10,k5,k1]
kingaku = [500,100,50,10,5,1]
money = int(input())
count = 0



for k in range(len(kingaku)):
	while(True):
		# print(money)
		if money - kingaku[k] < 0 or num[k] == 0:
			break
		money = money - kingaku[k]
		count = count + 1
		num[k] = num[k] - 1
print(count)