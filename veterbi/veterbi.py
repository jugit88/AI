lines = []
with open('penntree.tag','r') as sentences:
	lines.append('SSSS')
	for line in sentences:
		if line == '\n':
			lines.append('EEEE')
			lines.append('SSSS')
		else:
			lines.append(line.rstrip())
		lines.append('EEEE')
s = lines.count('\t')
print s
