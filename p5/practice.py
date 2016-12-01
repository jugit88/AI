from random import choice
lst = [0,2,1]
j = 1
for i in range(0,len(lst)):
	if i == j:
		lst[i] = 5
print choice(lst)

