import sys
edge = []
vertex = []
class Graph:
	def __init__(self):
	   self.vertices = {}
	   self.heurVal = {}
	   self.Open = []
	   # self.parent = None
	   self.solved = False
	   self.distance = 0
	   self.key = ''
	   self.parent = None


	def addVertex(self, value,estDist):
		#check if value already exists
		if value in self.vertices:
			print "Vertex already exists"
		else:
			# a = Graph()
			# a.key = value
			self.vertices[value] = []
			self.heurVal[value] = estDist

	def findVertex(self,value):
		if value in self.vertices:
			print self.vertices[value], self.heurVal
		else:
			print("Not found.")
	def addEdge(self, value1, value2,dist):
		a = Graph()
		b = Graph()
		a.key = value1
		b.key = value2
		if value1 not in self.vertices or value2 not in self.vertices:
			print "One or more vertices not found."
		else:
			# b = Graph()
			adjlst = self.vertices[value1]
			adjlst.append((value2,dist))
	
	# def getMin(self,node):
	# 	Min = min(self.vertices[node])
	# 	dist = sys.maxint
	# 	if self.vertices[Min[0]] == []:
	# 		for v in self.vertices[node]:
	# 			if v[1] < dist and self.vertices[v[0]] != []:
	# 				dist = v[1]
	# 				Min = v
	# 	# print Min
	# 	return Min

	'''def Dijkstra(self,start,end):
		if start == None or end == None:
			return
		if self.vertices[start] == None:
			return
		startV = Graph()
		endV = (Graph)
		startV.key = start
		endV.key = end
		distance = 0
		solved = [start]
		while (not endV.solved):
			minDist = sys.maxint
			solvedV = Graph()
			solvedV.key = None
			for s in solved:
				for v in self.vertices[s]:
					if (v[0] not in solved):
						dist = v[1] + distance
						if dist < minDist:
							solvedV.key = v[0]
							minDist = dist
							parent = s
		solvedV.distance = minDist
		# 		if s == end:
		# 			break
		# 		minVertex = min(self.vertices[s])
		# 		# print minVertex
		# 		# New Addition to add for an undirected graph 
		# 		# At the moment not working: need to check on this further
		# 		if minVertex[0] in solved:
		# 			for v in self.vertices[s]:
		# 				if v[1] < dist1 and v[0] not in solved:
		# 					dist1 = v[1]
		# 					minVertex = v
		# 		print self.vertices['B']

		# 		# dist1 = sys.maxint
		# 		# if vertex leads to dead end due to tiebreaker
		# 		# if self.vertices[minVertex[0]] == []:
		# 		# 	for v in self.vertices[s]:
		# 		# 		if v[1] < dist and self.vertices[v[0]] != []:
		# 		# 			dist = v[1]
		# 		# 			minVertex = v
		# 		if minVertex[0] not in solved:
		# 			dist = minVertex[1] + distance 
		# 			if (dist < minDist):
		# 				solvedV = minVertex[0]
		# 				minDist = dist
		# 				distance = dist
		# 				solved.append(solvedV)
		# 				print solved, minDist
		# return (solved,minDist)'''
							

	def getFn(self,node):
		dist = sys.maxint
		fPair = None
		for i in self.vertices[node]:
			# if self.vertices[i[0]] == []:
			# 	for j in self.vertices[node]:
			# 		if j[1] + self.heurVal[j[0]] < dist 
			# print self.vertices[i[0]]
			if i[0] == 'F':
				dist = i[1] + self.heurVal[i[0]]
				fPair = (i[0],dist,i[1])
			elif i[1] + self.heurVal[i[0]] < dist and self.vertices[i[0]] != []:
				dist = i[1] + self.heurVal[i[0]]
				fPair = (i[0],dist,i[1])
		# print fPair
		return fPair
	def aStar(self,start,end):
		if start == None or end == None:
			return
		if self.vertices[start] == None:
			return
		distance = 0
		distance1 = 0
		distList = []
		solved = [start]
		while (end not in solved):
			minDist = sys.maxint
			minDist1 = sys.maxint
			solvedV = None
			for s in solved:
				if s == end:
					break
				minVertex = self.getFn(s)
				if minVertex[0] not in solved:
					dist = minVertex[1] + distance
					dist1 = minVertex[2] + distance1
					if (dist < minDist):
						solvedV = minVertex[0]
						minDist = dist
						distance = dist
						minDist1 = dist1
						distance1 = dist1
						# print minDist1
						solved.append(solvedV)
		return (solved,minDist1)
		# print solved
		# print minDist1					


def fetchData():
	f = open(sys.argv[1],'r')
	print "File name:", f.name
	line = f.read()
	# line = line.strip('\n')
	# print line
	contents = line.split()
	for i in range(0,len(contents)):
		if '=' in contents[i]: 
			vertex.append((contents[i][0],int(contents[i][2:])))
		else:	
			edge.append((contents[i][1],contents[i][3],int(contents[i][5])))
			edge.append((contents[i][3],contents[i][1],int(contents[i][5])))
	f.close()

fetchData()
print edge
# print edge
for i in range(0,len(vertex)):
	g = Graph()
	g.addVertex(vertex[i][0],vertex[i][1])
for i in range(0,len(edge)):
	g.addEdge(edge[i][0],edge[i][1],edge[i][2])
def prettyPrint():

	dpath = g.Dijkstra('S','F')
	dpath1 = str(dpath[0])
	dpath1 = dpath1.replace(',',' ->')
	dpath1 = dpath1.replace("'",'')
	apath = g.aStar('S','F')
	apath1 = str(apath[0])
	apath1 = apath1.replace(',',' ->')
	apath1 = apath1.replace("'", '')

	print 'Shortest Path Algorithms'
	print 'Path | Distance | Nodes Evaluated'
	print 'Dijkstra:',dpath1 + ' |', dpath[1],'|',len(dpath[0])
	print 'A*:', apath1 + ' |', apath[1] ,'|',len(apath[0])
# prettyPrint()
# print g.Dijkstra('S','F')

