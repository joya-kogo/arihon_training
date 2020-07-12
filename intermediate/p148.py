import copy
n = 4
w = [2,1,3,2]
v = [3,2,4,2]
W = 5

wv1 = []
wv2 = []
def dfs1(i,wn,vn,flag):
	if flag is True:
		wn.append(w[i])
		vn.append(v[i])
	if i == int(n/2-1):
		wv1.append([sum(wn),sum(vn)])
		return 
	dfs1(i+1,copy.deepcopy(wn),copy.deepcopy(vn), True)
	dfs1(i+1,copy.deepcopy(wn),copy.deepcopy(vn), False)

def dfs2(i,wn,vn,flag):
	if flag is True:
		wn.append(w[i])
		vn.append(v[i])
	if i == int(n-1):
		wv2.append([sum(wn),sum(vn)])
		return 
	dfs2(i+1,copy.deepcopy(wn),copy.deepcopy(vn), True)
	dfs2(i+1,copy.deepcopy(wn),copy.deepcopy(vn), False)

dfs1(0,[],[],True)
dfs1(0,[],[],False)
dfs2(2,[],[],True)
dfs2(2,[],[],False)
wv1 = sorted(wv1)
wv2 = sorted(wv2)
print(wv1,wv2)

res = 0
m = 0
for i in range(len(wv1)):
	key = W - wv1[i][0]
	ub = len(wv2)
	lb = -1
	while ub - lb > 1:
		mid = int((ub+lb)/2)
		if key <= wv2[mid][0]:
			ub = mid
		else:
			lb = mid
	if(wv1[i][0]+wv2[ub][0] <= W and m < wv1[i][1] + wv2[ub][1]):
		m = wv1[i][1] + wv2[ub][1]
print(m)
