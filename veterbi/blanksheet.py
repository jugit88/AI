from __future__ import division 
from  collections import defaultdict
# import fnmatch
f = open('penntree.tag','r')
start = 'SSSS'
end = 'EEEE'
#initialize data 
t_prob = defaultdict(dict)
e_prob = defaultdict(dict)
lines = [(start,start)]
t_check = {}
e_check = {}
set_words = [start]
tags = [start]
tag_count = {start:1}
word_tag_count = {(start,start):1}
start_prob = {start:1}
readfile = f.readlines()
f.close()
# parse file into tuples of (word, TAG) format
for line in readfile:
	if line == '\n':
		lines.append((end,end))
		lines.append((start,start))
		tags.append(end)
		tags.append(start)
		tag_count[end] = 1
		word_tag_count[(end,end)] = 1
		word_tag_count[(start,start)] += 1
		set_words.append(end)
		set_words.append(start)
	else:
		for letter in line:
			if letter == '\t':
				delim = line.index(letter)
				word_tag = (line[:delim],line[delim+1:].rstrip('\n'))
				tag_only = line[delim+1:].rstrip('\n') 
				lines.append(word_tag)
				tags.append(tag_only)
				set_words.append(line[:delim])
				if word_tag not in word_tag_count:
					word_tag_count[word_tag] = 1
				else:
					word_tag_count[word_tag] += 1
				if tag_only not in tag_count:
					tag_count[tag_only] = 1
				else:
					tag_count[tag_only] += 1
lines.append((end,end))
tags.append(end)
states = set(tags)
set_words = set(set_words)
# create start probability dict
for i in states:
	if i != start:
		start_prob[i] = 0
tag_count[end] += 1
word_tag_count[(end,end)] += 1
# transition/emission probability 
b = 1
c = 0
e_prob[lines[0][1]][lines[0][0]] = 1
e_check[(start,start)] = 1
for i in range(1,len(lines)):
	 if lines[i][0] == lines[i][1]:
		e_prob[lines[i][1]][lines[i][0]] = 1
		e_check[(lines[i][1],lines[i][0])] = 1

	 else:
	 	e_prob[lines[i][1]][lines[i][0]] = word_tag_count[lines[i]] / tag_count[lines[i][1]]
	 	e_check[(lines[i][1],lines[i][0])] = 1
	 if (lines[i-1][1],lines[i][1]) not in t_check:
	 	t_prob[lines[i-1][1]][lines[i][1]] = 1
	 	t_check[(lines[i-1][1],lines[i][1])] = 1
	 else:
	 	t_prob[lines[i-1][1]][lines[i][1]] += 1
# print t_prob['NN']['DT'] / tags.count('NN')

for s in t_prob:
	for s1 in t_prob[s]:
		t_prob[s][s1] = t_prob[s][s1] / tag_count[s]

#fill the rest of the values in for transition and emission
for t in states:
	for t1 in states:
		if (t,t1) not in t_check:
			t_prob[t][t1] = 0
# for w in lines:
# 	if w[0] not in set_words:
# 		set_words.append(w[0])
# # print len(set_words)
for t in states:
	for w in set_words:
		if (t,w) not in e_check:
			e_prob[t][w] = 0
# print e_prob['DT']['This']
# for st in states:
# a = ['PDT', 'RBS', 'RBR', 'CD', 'EEEE', 'EX', 'IN', 'SSSS', 'MD', 'NNPS', '-RRB-', 'JJS', 'JJR', 'SYM', 'UH']
# print len(a)
# if ('This','RBS') in lines:
# 	print 1
	# print e_prob[st]['This']
# for st in states:


# tests
# print t_prob['NN']['DT']
# emission probability
# for w in lines:
# # 	# TODO: add other edge cases
# # 	# if w[0] == w[1] and w not in s_check:	#word is also a state
# # 	# 	e_prob[w[0]][w[1]] == 1
# # 	# else:
# 	e_prob[w[0]][w[1]] = lines.count(w) / tag_count[w[1]]
	# s_check.append(w)
# tests
# print lines.count(('the','DT')) / tags.count('DT')
# print t_prob

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    # print emit_p[start][obs[0]]

    for st in states:
        # if (st,obs[0]) in e_check:
        # 	st
        # else:
        # 	emit_p[st][obs[0]] = 0
        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}
    # Run Viterbi when t > 0

    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = max(V[t-1][prev_st]["prob"]*trans_p[prev_st][st] for prev_st in states)
            for prev_st in states:
                if V[t-1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                   
                    max_prob = max_tr_prob * emit_p[st][obs[t]]
                    V[t][st] = {"prob": max_prob, "prev": prev_st}
                    break
    for line in dptable(V):
        print line

    opt = []
    # The highest probability
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None
    # Get most probable state and its backtrack
    for st, data in V[-1].items():
        print st, data
        if data["prob"] == max_prob:
            opt.append(st)
            previous = st
            break
    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]

    print 'The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % max_prob

def dptable(V):
     # Print a table of steps from dictionary
     yield " ".join(("%12d" % i) for i in range(len(V)))
     for state in V[0]:
         yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)

if __name__ == "__main__":
    
    observations = (start, 'This', 'might', 'produce', 'a', 'result', 'if', 'the', 'system', 'works', 'well', '.', end)
    start_probability = start_prob
    transition_probability = t_prob
   
    emission_probability = e_prob
    viterbi(observations, states, start_probability, transition_probability, emission_probability)