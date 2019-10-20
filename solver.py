#Solving Einstein's Puzzle with Genetic Algorithm
import random
import copy
import time


n_population = 100000
liveness = 200
mutants = 200
fail_puntos = 0.5
punish_puntos = 1
liveness_probability = 70


colores = 		["roja","verde", "negra", "amarilla", "azul"]
profesiones = 	["matematico", "hacker", "analista", "desarrollador", "ingeniero"]
lenguajes = 	["python", "java", "javascript", "c#", "c++"]
ide = 			["vscode", "atom", "notepad++", "sublime", "vim"]
nosql = 		["cassandra", "redis", "hadoop", "neo4j", "mongo"]

matrizProto = [colores, profesiones, lenguajes, ide, nosql]

class matriz:

	def __init__(self):
		self.matriz = [[0 for x in range(5)] for x in range(5)] 
		self.puntos = 20
		self.approve = 0

	def getmatriz(self, x, y):
		return self.matriz[x][y]

	def randFill(self):
		for x in range(0,5):
			for y in range(0,5):
				self.matriz[x][y] = random.sample(matrizProto[x], 1)[0] 
				pass
			pass

	def mutate(self):
		x  = random.randint(0,4)
		y = random.randint(0,4)
		temp = self.matriz[x][y]
		self.matriz[x][y] = self.matriz[x][(y+1)%5]
		self.matriz[x][(y+1)%5] = temp
		random.shuffle(self.matriz[x])

		#self.matriz[x][y] = random.sample(matrizProto[x], 1)[0]
		#self.matriz[x][(y+1)%5] = random.sample(matrizProto[x], 1)[0]

	def test(self):
		#Check consistency
		for x in range(0,5):
			if len(self.matriz[x])!=len(set(self.matriz[x])):
				self.puntos -= 2*punish_puntos;
			pass

		##########################################################
		# El matemático vive en la casa roja
		try:
			i = self.matriz[1].index('matematico')
			if self.matriz[0][i] == 'roja':
				# print('El matemático vive en la casa roja')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El hacker programa en python
		try:
			i = self.matriz[1].index('hacker')
			if self.matriz[2][i] == 'python':
				# print('El hacker programa en python')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El que vive en la casa verde codea en vscode
		try:
			i = self.matriz[0].index('verde')
			if self.matriz[3][i] == 'vscode':
				# print('El que vive en la casa verde codea en vscode')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El analista usa Atom
		try:
			i = self.matriz[1].index('analista')
			if self.matriz[3][i] == 'atom':
				# print('El analista usa Atom')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El que vive en la casa verde está a la derecha del de la casa negra
		try:
			i = self.matriz[0].index('verde')
			if self.matriz[0][i-1] == 'negra' and i != 0:
				# print('El que vive en la casa verde está a la derecha del de la casa negra')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El que usa Redis codea en java
		try:
			i = self.matriz[4].index('redis')
			if self.matriz[2][i] == 'java':
				# print('El que usa redis codea en java')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El que usa Cassandra vive en la casa amarilla
		try:
			i = self.matriz[4].index('cassandra')
			if self.matriz[0][i] == 'amarilla':
				# print('El que usa cassandra vive en la casa amarilla')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El que usa notepad++ vive en la casa del medio (la 3)
		try:
			if self.matriz[3][2] == 'notepad++':
				# print('El que usa notepad++ vive en la casa del medio')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos
		
		# El desarrollador vive en la primera casa
		try:
			if self.matriz[1][0] == 'desarrollador':
				# print('El desarrollador vive en la primera casa')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El que usa hadoop vive al lado del que codea javascript
		try:	
			i = self.matriz[4].index('hadoop')
			if (self.matriz[2][i-1] == 'javascript' and i != 0) or (self.matriz[2][i+1] == 'javascript' and i != 4):
				# print('El que usa hadoop vive al lado del de js')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El que programa en c# vive al lado del que usa cassandra
		try:
			i = self.matriz[2].index('c#')
			if (self.matriz[4][i+1] == 'cassandra' and i != 4) or (self.matriz[4][i-1] == 'cassandra' and i != 0):
				# print('El que programa en c# vive a la izq del que usa cassandra')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El que usa Neo4J usa sublime
		try:
			i = self.matriz[4].index('neo4j')
			if self.matriz[3][i] == 'sublime':
				# print('El que usa neo4j usa sublime')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El ingeniero usa mongo
		try:
			i = self.matriz[1].index('ingeniero')
			if self.matriz[4][i] == 'mongo':
				# print('El ingeniero usa mongodb')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El desarrollador vive al lado del de la casa azul
		try:
			i = self.matriz[0].index('azul')
			if (self.matriz[1][i+1] == 'desarrollador' and i != 4) or (self.matriz[1][i-1] == 'desarrollador' and i != 0):
				# print('El desarrollador vive al lado del de la casa azul')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		# El programador de c++ lo hace en vim
		try:
			i = self.matriz[2].index('c++')
			if self.matriz[3][i] == 'vim':
				# print('El programador de c++ lo hace en vim')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_puntos
		except:
			self.puntos -= punish_puntos

		#print(self.matriz)
		#print(self.puntos)

class Puzzle:

	def __init__(self):
		 self.population = []

	def solve(self):

		self.generate(n_population)
		x = 0

		while True:
			x += 1
			print('Iteration  %d' %x)
			self.test()
			approve =  self.population[0].approve
			self.crossOver(liveness, n_population)
			self.mutate()
			

			if approve >= 15:
				break
			pass

		self.test()
		print(self.population[0].matriz)
		print(self.population[0].approve)

	def mutate(self):
		for x in range(0,mutants):
			y = random.randint(0,len(self.population)-1)
			self.population[y].mutate()
			pass
		

	def generate(self, i):
		for x in range(0,i):
			newborn = matriz()
			newborn.randFill()
			self.population.append(newborn)
			pass

	def crossOver(self, i, limit):
		
		goodPopulation = []
		i = 0
		while len(goodPopulation)<liveness:
			if random.randint(0,100)<liveness_probability:
				goodPopulation.append(self.population[i])
			i += 1 
			i %= len(self.population)

		newGeneration = []
		while len(newGeneration) <= limit:
			first = goodPopulation[random.randint(0,len(goodPopulation)-1)]
			second = goodPopulation[random.randint(0,len(goodPopulation)-1)]
			third = goodPopulation[random.randint(0,len(goodPopulation)-1)]
			newborn = self.cross(first, second, third)
			newGeneration.append(newborn)

		self.population = newGeneration

	def cross(self, first, second, third):
		newborn = matriz()
		#newborn.randFill()
		for x in range(0,5):
			for y in range(0,5):

				i = random.randint(0,2)
				if i == 0:
					newborn.matriz[x][y] = first.getmatriz(x,y)
				elif i == 1:
					newborn.matriz[x][y] = second.getmatriz(x,y)
				else:
					newborn.matriz[x][y] = third.getmatriz(x,y)
				pass
			pass
		return newborn

	def test(self):
		for x in range(0,len(self.population)):
			self.population[x].test()
			pass

		self.population.sort(key=lambda x: x.puntos, reverse=True)
		for x in range(0,1):
			print(self.population[x].approve)
			print(self.population[x].matriz)
			pass


puz = Puzzle()
puz.solve()