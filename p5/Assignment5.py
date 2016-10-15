# Jeremy Udis
# 10-14-2016
# Simulated annealing and Genetic Algorithm 
# Gerrymandering simulation
from __future__ import division
import sys
from random import randint,choice,shuffle
from collections import defaultdict
import math


class Sim_Annealing:
	def __init__(self,state_size):
		self.district = defaultdict(list)
		self.dragon = False
		self.matrix = [[0 for x in range(state_size)] for y in range(state_size)]
		self.marked = False
		self.district_num = 0
		self.adjlst = []
	def generate_districts(self,state_size):
		#generate neighboring solutions by checking edges and swapping them
		# check to see if the node is marked and the random index doesn't hit edge/corner cases
		x = randint(0,state_size-1)
		y = randint(0,state_size-1)
		while (self.matrix[x][y].marked):
			x = randint(0,state_size-1)
			y = randint(0,state_size-1)
		# x = 6
		# y = 2

		
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
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district or self.matrix[x+item[0]][y+item[1]].marked:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
				offset = lst[0]
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
					# TODO:check that every node in district is contiguous
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
							self.matrix[x][y].marked = True
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
							self.matrix[x+offset[0]][y+offset[1]].marked = True
				
			# print self.district[old_district]
		elif x == 0 and y != state_size-1 and y != state_size-1:
			lst = [(0,1),(1,0),(0,-1)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district or self.matrix[x+item[0]][y+item[1]].marked:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = lst[0]
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
						
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
							self.matrix[x][y].marked = True
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
							self.matrix[x+offset[0]][y+offset[1]].marked = True
			# print self.district[new_district]
		elif x == 0 and y == state_size-1:
			lst = [(1,0),(0,-1)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district or self.matrix[x+item[0]][y+item[1]].marked:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = lst[0]
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				o_dist = self.district[old_district][:]
				n_dist = self.district[new_district][:]
				for i in range(0,len(self.district[new_district])):
						# if ((n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]+1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]+1)):
						# 	return
						# if ((o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]+1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]+1)):
						# 	return
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
							self.matrix[x][y].marked = True
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
							self.matrix[x+offset[0]][y+offset[1]].marked = True
				# print self.district[old_district]
		elif x == state_size-1 and y == 0:
			lst = [(0,1),(-1,0)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district or self.matrix[x+item[0]][y+item[1]].marked:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = lst[0]
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				o_dist = self.district[old_district][:]
				n_dist = self.district[new_district][:]
				for i in range(0,len(self.district[new_district])):
						# if ((n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]+1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]+1)):
						# 	return
						# if ((o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]+1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]+1)):
						# 	return
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
							self.matrix[x][y].marked = True
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
							self.matrix[x+offset[0]][y+offset[1]].marked = True
		elif x == state_size-1 and y == state_size-1:
			lst = [(0,-1),(-1,0)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district or self.matrix[x+item[0]][y+item[1]].marked:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = lst[0]
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				o_dist = self.district[old_district][:]
				n_dist = self.district[new_district][:]
				for i in range(0,len(self.district[new_district])):
						# if ((n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]+1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]+1)):
						# 	return
						# if ((o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]+1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]+1)):
						# 	return
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
							self.matrix[x][y].marked = True
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
							self.matrix[x+offset[0]][y+offset[1]].marked = True
		elif x == state_size-1 and y != 0 and y != state_size-1:
			lst = [(0,1),(0,-1),(-1,0)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district or self.matrix[x+item[0]][y+item[1]].marked:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = lst[0]
				
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				o_dist = self.district[old_district][:]
				n_dist = self.district[new_district][:]
				for i in range(0,len(self.district[new_district])):
						# if ((n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]+1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]+1)):
						# 	return
						# if ((o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]+1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]+1)):
						# 	return
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
							self.matrix[x][y].marked = True
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
							self.matrix[x+offset[0]][y+offset[1]].marked = True
		elif x != 0 and x != state_size-1 and y == 0:
			lst = [(0,1),(-1,0),(1,0)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district or self.matrix[x+item[0]][y+item[1]].marked:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
				
			if lst != []:
					
				# print lst[0]
				offset = lst[0]
				n_dist = self.district[new_district][:]
				o_dist = self.district[old_district][:]
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				for i in range(0,len(self.district[new_district])):
						
						# if ((n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]+1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]+1)):
						# 	return
						# if ((o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]+1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]+1)):
						# 	return
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							# print self.district[new_district][i]
							self.matrix[x][y].district_num = old_district
							self.matrix[x][y].marked = True
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
							self.matrix[x+offset[0]][y+offset[1]].marked = True
		elif x != state_size-1 and x != 0 and y == state_size-1:
			lst = [(0,-1),(-1,0),(1,0)]
			rm = []
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district or self.matrix[x+item[0]][y+item[1]].marked:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = lst[0]
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				n_dist = self.district[new_district][:]
				o_dist = self.district[old_district][:]
				for i in range(0,len(self.district[new_district])):
						# if ((n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]+1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]+1)):
						# 	return
						# if ((o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]-1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]+1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]+1)
						# or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]+1)):
						# 	return
						if self.district[new_district][i] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon):
							self.district[new_district][i] = (x,y,self.matrix[x][y].dragon)
							self.matrix[x][y].district_num = old_district
							self.matrix[x][y].marked = True
						if self.district[old_district][i] == (x,y,self.matrix[x][y].dragon):
							self.district[old_district][i] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
							self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
							self.matrix[x+offset[0]][y+offset[1]].marked = True

		else:
			lst = [(0,-1),(-1,0),(1,0),(0,1)]
			rm = []
			# print x,y
			for item in lst:

				# print item
				new_district = self.matrix[x + item[0]][y + item[1]].district_num
				# print new_district
				if self.matrix[x + item[0]][y + item[1]].dragon == self.matrix[x][y].dragon or old_district == new_district or self.matrix[x+item[0]][y+item[1]].marked:
					# print item
					rm.append(item)
			for i in rm:
				if i in lst:
					lst.remove(i)	
			# TODO:check there offset is in adjacent list of any item in new district
			if lst != []:
					
				offset = lst[0]
				# print offset
				new_district = self.matrix[x + offset[0]][y + offset[1]].district_num
				# print new_district,old_district
				n_dist = self.district[new_district][:]
				o_dist = self.district[old_district][:]

				for i in range(1,len(self.district[new_district])):
					if ((n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]-1)
						or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]-1,n_dist[i][1]+1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]-1) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]) or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0],n_dist[i][1]+1)
						or (n_dist[i-1][0],n_dist[i-1][1]) != (n_dist[i][0]+1,n_dist[i][1]+1)):
							return
					if ((o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]-1)
						or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]-1,o_dist[i][1]+1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]-1) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]) or (o_dist[i-1][0],o_dist[i-1][1]) != (o_dist[i][0],o_dist[i][1]+1)
						or (n_dist[i-1][0],n_dist[i-1][1]) != (o_dist[i][0]+1,o_dist[i][1]+1)):
							return
					assert(self.district[new_district][i+1] == (x,y+1,self.matrix[x][y+1].dragon) or (x+1,y,self.matrix[x+1][y].dragon) or (x-1,y,self.matrix[x-1][y].dragon) or (x,y-1,self.matrix[x][y-1].dragon))
					if self.district[new_district][i-1] == (x + offset[0],y + offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon) and (x,y) in self.matrix[x + offset[0]][y + offset[1]].adjlst:
						self.district[new_district][i-1] = (x,y,self.matrix[x][y].dragon)
						self.matrix[x][y].district_num = old_district
						self.matrix[x][y].marked = True
					if self.district[old_district][i-1] == (x,y,self.matrix[x][y].dragon) and (x+offset[0],y+offset[1]) in self.matrix[x][y].adjlst:
						self.district[old_district][i-1] = (x+offset[0],y+offset[1],self.matrix[x+offset[0]][y+offset[1]].dragon)
						self.matrix[x+offset[0]][y+offset[1]].district_num = new_district
						self.matrix[x+offset[0]][y+offset[1]].marked = True

		
	def countDistricts(self,state_size):
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
		return (dragon_districts,rabbit_districts,neutral_districs)
	def simulatedAnnealing(self,state_size,T,k):
		# need to populate matrix before calling on self.district
		ratio = self.populateMatrix(sys.argv[1],state_size)
		# print ratio
		rabbit_ratio = ratio[0]/100
		district_locations = self.district
		initial_district_count = self.countDistricts(state_size)
		# print self.district[0]
		# print initial_district_count
		s = initial_district_count[1]/(state_size - initial_district_count[2])
		Tmin = .0001
		alpha = 0.1
		equilibrium = 0
		search_states = []
		# dis_count = initial_district_count
		# search_num = 0
		while T > Tmin:
			while equilibrium != 1000:
				# new_district_count = self.countDistricts(state_size)
				self.generate_districts(state_size)
				new_district_count = self.countDistricts(state_size)
				if new_district_count not in search_states:
					search_states.append(new_district_count)
				s_prime = new_district_count[1]/(state_size-new_district_count[2])
				# want to get as close to the population as possible with fitness function
				if abs(1 - (s_prime/rabbit_ratio)) < abs(1 - (s/rabbit_ratio)):
					s = s_prime 	#accept neighbor solution
					# cache district locations
					# print s
					district_locations = self.district
					initial_district_count = new_district_count
					# print district_locations
				else:
					prob_sprime = math.exp(new_district_count[1]/(k * T)) 	# accept sprime w/probability  
				equilibrium += 1
			T = T * alpha
		# for i in range(0,10):
		# 	for j in range(0,10):
		# 		print self.matrix[i][j].district_num
		# print s,district_locations
		return (district_locations,len(search_states),initial_district_count,ratio)
			# else the district is rabbit
		
		# district_display = 'Number of districts with a majority for each party:\n************************************* \nR:<{0}>\nD:<{1}> N:<{2}>'.format(rabbit_districts,dragon_districts,neutral_districs)
		# print district_display
	def populateMatrix(self,arg,state_size):
		f = open(arg,'r')
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
				node.marked = False
				district_index = self.district[i]
				district_index.append((i,j,node.dragon))
		# print self.district
		f.close()
		percent_dragons = (num_dragons/(state_size * state_size)) * 100
		percent_rabbits = 100 - percent_dragons
		return (percent_rabbits,percent_dragons)

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
f = open(sys.argv[1],'r')
line = f.read()
line = line.replace(' ', '')
contents = line.split()
size = len(contents[0])
f.close()

m = Sim_Annealing(size)
# m.populateMatrix(sys.argv[1],10)
# for i in range(0,20):	
# 	m.generate_districts(10)
tuple = m.simulatedAnnealing(size,100,10)
# print m.matrix[0][0].district_num

# population = m.populateMatrix(sys.argv[1],10)
percent_display = "Party division in population: \n************************************* \nR:<% {0}>\nD:<% {1}> \n************************************* \n".format(tuple[3][0],tuple[3][1])
print percent_display
# run simulated annealing

# count_districts = m.countDistricts(10)	

district_display = 'Number of districts with a majority for each party:\n************************************* \nR:<{0}>\nD:<{1}> \n************************************* \n'.format(tuple[2][1],tuple[2][0])
print district_display
location_array = [[0 for x in range(size)] for y in range(size)]

for i in tuple[0]:
	for j in range(0,size):
		location_array[i][j] = tuple[0][i][:][j][:2]
	# print location_array
location_display = 'Locations assigned to each district \n************************************* \n District 1: {0}\n District 2: {1} \n District 3: {2} \n District 4: {3} \n District 5: {4} \n District 6: {5} \n District 7: {6} \n District 8: {7} \n'.format(location_array[0],location_array[1],location_array[2],location_array[3],location_array[4],location_array[5],location_array[6],location_array[7])
if size == 8:
	print location_display.replace('[','').replace(']','')
else:
	location_display1 = location_display + ' District 9: {0} \n District 10: {1}'.format(location_array[8],location_array[9]) 
	print location_display1.replace('[','').replace(']','')
state_display = '************************************* \n Algorithm applied:<SA> \n ************************************* \n \n ************************************* \n Number of search states explored:<{0}> \n ************************************* '.format(tuple[1])
print state_display


