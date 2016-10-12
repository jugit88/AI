# Jeremy Udis
# 10-14-2016
# Simulated annealing and Genetic Algorithm 
# Gerrymandering simulation
from __future__ import division
import sys
from random import randint
from collections import defaultdict


class Sim_Annealing:
	def __init__(self,state_size):
		self.district = defaultdict(list)
		self.dragon = False
		self.matrix = [[0 for x in range(state_size)] for y in range(state_size)]
	def generate_districts(self,state_size):
		#generate neighboring solutions by checking edges and swapping them

		# count majority districts
		dragon_districts = 0
		rabbit_districts = 0
		neutral_districs = 0
		# print self.district
		for i in self.district:
			_dragon = 0
			index = self.district[i]
			for j in index:
				if j[2]:	# boolean value. True:Dragon False:Rabbit
					_dragon += 1
			if _dragon > state_size/2:
				dragon_districts += 1
			elif _dragon == state_size/2:
				neutral_districs += 1
			else:
				rabbit_districts += 1
			# else the district is rabbit




		
		district_display = 'Number of districts with a majority for each party:\n************************************* \nR:<{0}>\nD:<{1}>'.format(rabbit_districts,dragon_districts)
		print district_display
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
				# create initial districts
				district_index = self.district[i]
				district_index.append((i,j,node.dragon))
		# print self.district

		percent_dragons = (num_dragons/(state_size * state_size)) * 100
		percent_rabbits = 100 - percent_dragons
		percent_display = "Party division in population: \n************************************* \nR:<% {0}>\nD:<% {1}>".format(percent_rabbits,percent_dragons)
		print percent_display
		# Generate Initial district partitions


m = Sim_Annealing(10)
m.populateMatrix(sys.argv[1],10)
m.generate_districts(10)




