import sys
edge = []
vertex = []
class Graph:
	def __init__(self):
	   self.verticies = {}
	   self.heurVal = {}
	   self.Open = []
	   self.parent = None


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
	def f(self,n):
		# for i in self.verticies[n]:
			# fn = i[1] + i.heurVal
			print self.heurVal[n]


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
g.aStar('A','D')
# g.f('C')
# print edge