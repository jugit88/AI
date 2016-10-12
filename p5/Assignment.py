# Jeremy Udis
# 10-14-2016
# Simulated annealing and Genetic Algorithm 
# Gerrymandering simulation

import sys
from random import randint

class Sim_Annealing:
	def __init__(self,grid_size):
		self.district = 0
		self.dragon = False
		self.matrix = [[0 for x in range (grid_size)] for y in range(grid_size)]
	def generate_districts(self):
		return
	def populateMatrix(self,arg):
		f = open(arg,'r')
		print "File Name:", f.name
		line = f.read()
		# for i in range(0,10):
			



