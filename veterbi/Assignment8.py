from __future__ import division
import collections
lines = []
t_prob = {}
# key = {}
t_prob1 = collections.defaultdict(dict)
tags = []
# t_prob1 = collections.defaultdict(dict)
with open('penntree.tag','r') as sentences:
    lines.append('SSSS')
    for line in sentences:
    	# line = line.rstrip('\t')
        if line == '\n':
            lines.append('EEEE')
            lines.append('SSSS')
        else:
            lines.append(line.rstrip())
lines.append('EEEE')

# build the tags array by finding index of \t within each substring
str_tags = ''
for item in lines:
	if item == 'SSSS' or item == 'EEEE':
		tags.append(item)
		str_tags += item
	for letter in item:
		if letter == '\t':
			tag_index = item.index(letter)
			# print tag_index
			tags.append(item[tag_index+1:])
			str_tags += item[tag_index+1:] 
# calculate transition probabilties from the tags list
# count = 0
# for i in range(1,len(tags)):
# 	if tags[i-1] == 'NN' and tags[i] == 'DT':
# 		count += 1

for i in range(1,len(tags)):
	t = tags[i-1]
	t1 = tags[i]
	# if t == 'EEEE' and t1 == 'SSSS': TODO:need this on emision prob not trans
	# 	t_prob[t+t1] = 0
		# t_prob[t] = t_prob1
		# t_prob1[t1] = 0
	if t + t1 not in t_prob:
		# t_prob[t] = t_prob1
		# t_prob1[t1] = str_tags.count(t+t1)/str_tags.count(t)
		t_prob[t+t1] = str_tags.count(t+t1)/str_tags.count(t)



print t_prob['VB-LRB']

# s = lines.count('the\tDT')
# print s
