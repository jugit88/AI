from __future__ import division 
from  collections import defaultdict
import fnmatch
f = open('penntree.tag','r')
start = 'SSSS'
end = 'EEEE'
t_prob = defaultdict(dict)
lines = [(start,start)]
check = []
tags = [start]
readfile = f.readlines()
for line in readfile:
	if line == '\n':
		lines.append((end,end))
		lines.append((start,start))
		tags.append(end)
		tags.append(start)
	else:
		for letter in line:
			if letter == '\t':
				delim = line.index(letter)
				lines.append((line[:delim],line[delim+1:].rstrip('\n')))
				tags.append(line[delim+1:].rstrip('\n'))
lines.append((end,end))
tags.append(end)
# transition probability 
for i in range(1,len(lines)):
	 if (lines[i-1][1],lines[i][1]) not in check:
	 	t_prob[lines[i-1][1]][lines[i][1]] = 1
	 	check.append((lines[i-1][1],lines[i][1]))
	 else:
	 	t_prob[lines[i-1][1]][lines[i][1]] += 1
print t_prob['NN']['DT'] / tags.count('NN')
# for s in t_prob:
# 	for s1 in t_prob[s]:
# 		t_prob[s][s1] = t_prob[s][s1] / tags.count(s)
# print t_prob['NN']['DT']

# readfile1 = start +'\n' + readfile
# readfile.readlines()	
# contents = readfile.split()
# print contents