# Jeremy Udis
# 10-14-2016
# Simulated annealing and Genetic Algorithm 
# Gerrymandering simulation
from __future__ import division
import sys
from random import randint,choice
from collections import defaultdict


class Sim_Annealing:
	def __init__(self,state_size):
		self.district = defaultdict(list)
		self.dragon = False
		self.matrix = [[0 for x in range(state_size)] for y in range(state_size)]
		# self.marked = False
		self.district_num = 0
		self.adjlst = []
	def generate_districts(self,state_size):
		#generate neighboring solutions by checking edges and swapping them
		# check to see if the node is marked and the random index doesn't hit edge/corner cases
		x = randint(0,state_size-1)
		y = randint(0,state_size-1)
		
		print x,y
		old_district = self.matrix[x][y].district_num
		# print self.district[old_district]
		# print self.district[old_district][:][:]
		if x == 0 and y == 0:
			# need to check if a) different political affiliation b) if those districts still contigous if swapped
			lst = [(0,1),(1,0)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = choice(lst)
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
				
			# print self.district[old_district]
		elif x == 0 and y != state_size-1 and y != state_size-1:
			lst = [(0,1),(1,0),(0,-1)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = choice(lst)
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
			# print self.district[new_district]
		elif x == 0 and y == state_size-1:
			lst = [(1,0),(0,-1)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = choice(lst)
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district

				# print self.district[old_district]
		elif x == state_size-1 and y == 0:
			lst = [(0,1),(-1,0)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = choice(lst)
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
		elif x == state_size-1 and y == state_size-1:
			lst = [(0,-1),(-1,0)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = choice(lst)
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district

		elif x == state_size-1 and y != 0 and y != state_size-1:
			lst = [(0,1),(0,-1),(-1,0)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = choice(lst)
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
		elif x != 0 and x != state_size-1 and y == 0:
			lst = [(0,1),(-1,0),(1,0)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = choice(lst)
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
		
		elif x != state_size-1 and x != 0 and y == state_size-1:
			lst = [(0,-1),(-1,0),(1,0)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = choice(lst)
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
		else:
			lst = [(0,-1),(-1,0),(1,0),(0,1)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = choice(lst)
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
		

		# count majority districts
		dragon_districts = 0
		rabbit_districts = 0
		neutral_districs = 0
		# print self.district
		for i in self.district:
			_dragon = 0
			index1 = self.district[i]
			for j in index1:
				if j[2]:	# boolean value. True:Dragon False:Rabbit
					_dragon += 1
			if _dragon > state_size/2:
				dragon_districts += 1
			elif _dragon == state_size/2:
				neutral_districs += 1
			else:
				rabbit_districts += 1
			# else the district is rabbit
		
		district_display = 'Number of districts with a majority for each party:\n************************************* \nR:<{0}>\nD:<{1}> N:<{2}>'.format(rabbit_districts,dragon_districts,neutral_districs)
		print district_display
		return self.district

	def populateMatrix(self,arg,state_size):
		f = open(arg,'r')
		print "File Name:", f.name
		line = f.read()
		line = line.replace(' ', '')
		contents = line.split()
		# Populate matrix with 'D' or 'R'
		num_dragons = 0
		for i in range(0,state_size):
			for j in range(0,state_size):
				node = Sim_Annealing(state_size)
				self.matrix[i][j] = node
				# node.contents[i][j]
				if contents[i][j] == 'D':
					node.dragon = True
					num_dragons += 1
				# print node.dragon
				# create initial districts
				if i == 0 and j == 0:
					node.adjlst = [(0,1),(1,0),(1,1)]
				elif i == 0 and j == state_size - 1:
					node.adjlst = [(0,state_size-1),(state_size+1,0),(state_size+1,state_size-1)]
				elif i == state_size -1 and j == 0:
					node.adjlst = [(state_size - 2,0),(state_size - 1,1),(state_size-2,1)]
				elif i == state_size-1 and j == state_size-1:
					node.adjlst = [(state_size - 2,state_size-1),(state_size - 1,state_size-2),(state_size-2,state_size-2)]
				elif i == 0 and j != 0 and j != state_size-1:
					node.adjlst = [(i,j-1),(i,j+1),(i+1,j),(i+1,j+1),(i+1,j-1)]
				elif i == state_size-1 and j != 0 and j != state_size-1:
					node.adjlst = [(i,j-1),(i,j+1),(i-1,j),(i-1,j+1),(i-1,j-1)]
				elif j == 0 and i != 0 and i != state_size-1:
					node.adjlst = [(i,j+1),(i+1,j),(i-1,j),(i+1,j+1),(i-1,j+1)]
				elif j == state_size-1 and i != 0 and i != state_size-1:
					node.adjlst = [(i,j-1),(i+1,j),(i-1,j),(i+1,j-1),(i-1,j-1)]
				else:
					node.adjlst = [(i,j+1),(i+1,j),(i,j-1),(i-1,j),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)]



				node.district_num = i
				district_index = self.district[i]
				district_index.append((i,j,node.dragon))
		# print self.district

		percent_dragons = (num_dragons/(state_size * state_size)) * 100
		percent_rabbits = 100 - percent_dragons
		percent_display = "Party division in population: \n************************************* \nR:<% {0}>\nD:<% {1}>".format(percent_rabbits,percent_dragons)
		print percent_display
		# Generate Initial district partitions


# n = Sim_Annealing(10)
# n.populateMatrix(sys.argv[1],10)
# n.generate_districts(10)
# m = Sim_Annealing(10)
# m.populateMatrix(sys.argv[1],10)
# m.generate_districts(10)

# m.populateMatrix(sys.argv[1],10)
# m = Sim_Annealing(10)
# m.populateMatrix(sys.argv[1],10)
m = Sim_Annealing(10)
m.populateMatrix(sys.argv[1],10)
for i in range(0,200):	
	m.generate_districts(10)
print m.district
	




