import sys

f = open(sys.argv[1],'rw')
print "File name: ", f.name
edge = {}
vertex = []
line = f.read()
line = line.strip('\n')
# print line
contents = line.split()

for i in range(0,len(contents)):
	# print contents[i]
	if '=' in contents[i]: 
		vertex.append((contents[i][0],int(contents[i][2:])))
	else:
		edge[contents[i][1]] = (contents[i][3],int(contents[i][5]))
print edge
f.close()
