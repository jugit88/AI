def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
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


def parseData(fileName):
	
	tempList = []
	sentences = []
	fo = open(fileName, "r")
	lines = fo.readlines()
	
	for line in lines:
		if line != "\n":
			tempList.append(line.split())
			
	
	i = 0
	j = 0
	while i < len(tempList):
		if tempList[i][1] == ".":
			t = []
			while j <= i:
				t.append(tempList[j])
				j += 1
			sentences.append(t)
		i += 1
	
	
	# list of sentences, which are lists of word tag pairs
	for s in sentences:
		s.insert(0, ["SSSS", "SSSS"])
		s.append(["EEEE", "EEEE"])
	
	
	
	words = []
	states = []
	
	print "Constructing list of unique words..."
	for s in sentences:
		for pair in s:
			if pair[0] not in words:
				words.append(pair[0])
	
				
	print "Constructing list of unique states..."
	for s in sentences:
		for pair in s:
			if pair[1] not in states:
				states.append(pair[1])
	
	counts = {}
	transCounts = {}
	emissionCounts = {}
	transProb = {}
	emissionProb = {}
	
	for s in sentences:
		for pair in s:
			if pair[1] in counts:
				counts[pair[1]] += 1
			else:
				counts[pair[1]] = 1
	
	print "Constructing transCounts..."
	for s in sentences:
		i = 0
		while i < len(s):
			tag = s[i][1]
			if i > 0:
				prevTag = s[i-1][1]
				if tag in transCounts:
					if prevTag in transCounts[tag]:
						transCounts[tag][prevTag] += 1
					else:
						transCounts[tag][prevTag] = 1
				else:
					transCounts[tag] = {}
					transCounts[tag][prevTag] = 1
			i += 1
			
	# construct trans probabilities
	for tag, tagsDict in transCounts.iteritems():
		for tag2, tagCount in tagsDict.iteritems():
			if tag2 in transProb:
				transProb[tag2][tag] = tagCount / float(counts[tag2])
			else:
				transProb[tag2] = {}
				transProb[tag2][tag] = tagCount / float(counts[tag2])
	
	# add 0 for trans probabilities of states not included
	for tag, tagDict in transProb.iteritems():
		for state in states:
			if state not in tagDict:
				tagDict[state] = 0.0 
	
	transProb["EEEE"] = {}
	# add trans probabilities for start tag
	for state in states:
		transProb[state]["SSSS"] = 0.0
		transProb["EEEE"][state] = 0.0
	
	# calculate emission counts [word and tag]
	for s in sentences:
		for pair in s:
			tag = pair[1]
			word = pair[0]
			if tag != "EEEE" and tag != "SSSS":
				if tag in emissionCounts:
					if word in emissionCounts[tag]:
						emissionCounts[tag][word] += 1
					else:
						emissionCounts[tag][word] = 1
				else:
					emissionCounts[tag] = {}
					emissionCounts[tag][word] = 1
	
			
	# construct emission prob
	for tag, wordDict in emissionCounts.iteritems():
		for word, wordCount in wordDict.iteritems():
			if tag in emissionProb:
				emissionProb[tag][word] = wordCount / float(counts[tag])
			else:
				emissionProb[tag] = {}
				emissionProb[tag][word] = wordCount / float(counts[tag])
	
	# add for emission probabilities for words not shown with tags
	for tag, wordDict in emissionProb.iteritems():
		for word in words:
			if word not in wordDict:
				wordDict[word] = 0.0
			
	
	# add emission probabilities for start and end tags
	emissionProb["SSSS"] = {}
	emissionProb["EEEE"] = {}
	
	for word in words:
		emissionProb["SSSS"][word] = 0.0
		emissionProb["EEEE"][word] = 0.0

	for state in states:
		emissionProb[state]["EEEE"] = 0.0
		emissionProb[state]["SSSS"] = 0.0
		
	
	
		
	emissionProb["SSSS"]["SSSS"] = 1.0
	emissionProb["EEEE"]["EEEE"] = 1.0
	

	
	#observation, and starting probabilities
	obs = ("SSSS", "This", "might", "produce", "a","result", "if","the","system", "works", "well",".","EEEE")
	startProb = {}
	for state in states:
		if state == "SSSS":
			startProb[state] = 1.0
		else:
			startProb[state] = 0.0
	
	print states
	viterbi(obs, states, startProb, transProb, emissionProb)
	


if __name__ == "__main__":
	parseData("penntree.tag")
    
 
