import sys
edge = []
vertex = []
class Graph:
	def __init__(self):
	   self.verticies = {}
	   self.heurVal = {}
	   self.Open = []
	   # self.parent = None
	   self.solved = False
	   self.distance = 0


	def addVertex(self, value,estDist):
		#check if value already exists
		if value in self.verticies:
			print "Vertex already exists"
		else:
			self.verticies[value] = []
			self.heurVal[value] = estDist

	def findVertex(self,value):
		if value in self.verticies:
			print self.verticies[value], self.heurVal
		else:
			print("Not found.")
	def addEdge(self, value1, value2,dist):
		a = Graph()
		if value1 not in self.verticies or value2 not in self.verticies:
			print "One or more vertices not found."
		else:
			adjlst = self.verticies[value1]
			adjlst.append((value2,dist))
	def aStar(self,start,end):
		self.Open.append(start)
		closed = []
		while not self.Open:
			node = min(self.Open)
			self.Open.remove(node)
			if node != end:
				closed.append(node)
				for n in self.verticies[node]:
					if n not in closed:
						fn = n[1] + self.heurVal[n]
						print fn
						n.parent = node
						if n in Open:
							print fn
						else:
							self.Open.append(n)
			else:
				break
	def getMin(self,node):
		Min = min(self.verticies[node])
		dist = sys.maxint
		if self.verticies[Min[0]] == []:
			for v in self.verticies[node]:
				if v[1] < dist and self.verticies[v[0]] != []:
					dist = v[1]
					Min = v
		# print Min
		return Min

	def Dijkstra(self,start,end):
		if start == None or end == None:
			return
		if self.verticies[start] == None:
			return
		distance = 0
		distList = []
		# minDist = sys.maxint
		solved = [start]
		while (end not in solved):
			minDist = sys.maxint
			solvedV = None
			for s in solved:
				minVertex = min(self.verticies[s])
				dist1 = sys.maxint
				if self.verticies[minVertex[0]] == []:
					for v in self.verticies[s]:
						if v[1] < dist1 and self.verticies[v[0]] != []:
							dist = v[1]
							minVertex = v
				# minVertex = node.getMin(self.verticies[s])
				if minVertex[0] not in solved:
					dist = minVertex[1] + distance 
					if (dist < minDist):
						solvedV = minVertex[0]
						minDist = dist
						distance = dist
						solved.append(solvedV)
						print solved
						print minDist					
				


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
	# print edge
	f.close()
fetchData()
g = Graph()
for i in range(0,len(vertex)):
	g.addVertex(vertex[i][0],vertex[i][1])
for i in range(0,len(edge)):
	g.addEdge(edge[i][0],edge[i][1],edge[i][2])
# print vertex
# g.findVertex('S')
# g.getMin('R')
g.Dijkstra('S','F')
# print edge