#Solving Einstein's Puzzle with Genetic Algorithm
import random
import copy

n_population = 100000
liveness = 200
mutants = 200
fail_score = 0.5
punish_score = 1
liveness_probability = 70

'''
1.
Hay cinco casas de diferentes colores, cinco profesiones distintas, cinco lenguajes de
programación, cinco editores de texto, cinco bases de datos NoSQL distintas.
2.
El matemático vive en la casa roja
3.
El hacker programa en Python
4.
Visual Studio Code es utilizado por el que vive en la casa verde
5.
El analista usa Atom
6.
El que vive en la casa verde, esta a la derecha del de la casa negra
7.
Es que usa Redis escribe en Java
8.
El que usa Cassandra vive en la casa amarilla
9.
El que usa Notepad ++ vive en la casa del medio
10.
El desarrollador vive en a primer casa
11.
El que usa Hadoop vive al lado del que escribe en JavaScript
12.
Cassandra es usado en la casa al lado del que programa en C#
13.
La persona que usa Neo4J usa SublimeText
14.
El ingeniero usa MongoDB
15.
El desarrollador vive al lado de la casa azul

¿Quién programa C++ en Vim
'''

colores = 		["roja","verde", "negra", "amarilla", "azul"]
profesiones = 	["matematico", "hacker", "analista", "desarrollador", "ingeniero"]
lenguajes = 	["python", "java", "javascript", "c#", "c++"]
ide = 			["vscode", "atom", "notepad++", "sublime", "vim"]
nosql = 		["cassandra", "redis", "hadoop", "neo4j", "mongo"]

matrizAux = [colores, profesiones, lenguajes, ide, nosql]

class Tabla:

	def __init__(self):
		self.matriz = [[0 for x in range(5)] for x in range(5)] 
		self.puntos = 20
		self.approve = 0
		self.encontrado = False

	def getMatriz(self, x, y):
		return self.matriz[x][y]

	def randFill(self):
		for x in range(0,5):
			for y in range(0,5):
				self.matriz[x][y] = random.sample(matrizAux[x], 1)[0] 
				pass
			pass

	def mutate(self):
		x  = random.randint(0,4)
		y = random.randint(0,4)
		temp = self.matriz[x][y]
		self.matriz[x][y] = self.matriz[x][(y+1)%5]
		self.matriz[x][(y+1)%5] = temp
		random.shuffle(self.matriz[x])

		#self.table[x][y] = random.sample(tableProto[x], 1)[0]
		#self.table[x][(y+1)%5] = random.sample(tableProto[x], 1)[0]

	def test(self):
		#Check consistency
		for x in range(0,5):
			if len(self.matriz[x])!=len(set(self.matriz[x])):
				self.puntos -= 2*punish_score
			pass

		##########################################################
		# El matemático vive en la casa roja
		try:
			i = self.matriz[1].index('matematico')
			if self.matriz[0][i] == 'roja':
				print('El matemático vive en la casa roja')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El hacker programa en python
		try:
			i = self.matriz[1].index('hacker')
			if self.matriz[2][i] == 'python':
				print('El hacker programa en python')
				self.puntos += 1
				self.approve += 1
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El que vive en la casa verde codea en vscode
		try:
			i = self.matriz[0].index('verde')
			if self.matriz[3][i] == 'vscode':
				print('El que vive en la casa verde codea en vscode')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El analista usa Atom
		try:
			i = self.matriz[1].index('analista')
			if self.matriz[3][i] == 'atom':
				print('El analista usa Atom')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El que vive en la casa verde está a la derecha del de la casa negra
		try:
			i = self.matriz[0].index('verde')
			if self.matriz[0][i+1] == 'negra':
				print('El que vive en la casa verde está a la derecha del de la casa negra')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El que usa Redis codea en java
		try:
			i = self.matriz[4].index('redis')
			if self.matriz[2][i] == 'java':
				print('El que usa redis codea en java')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El que usa Cassandra vive en la casa amarilla
		try:
			i = self.matriz[4].index('cassandra')
			if self.matriz[0][i] == 'amarilla':
				print('El que usa cassandra vive en la casa amarilla')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El que usa notepad++ vive en la casa del medio (la 3)
		try:
			i = self.matriz[3].index('notepad++')
			if self.matriz[3][2] == 'notepad++':
				print('El que usa notepad++ vive en la casa del medio')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score
		
		# El desarrollador vive en la primera casa
		try:
			i = self.matriz[1].index('desarrollador')
			if self.matriz[1][0] == 'desarrollador':
				print('El desarrollador vive en la primera casa')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El que usa hadoop vive al lado del que codea javascript [a la derecha]
		try:	
			i = self.matriz[4].index('hadoop')
			if self.matriz[2][i+1] == 'javascript':
				print('El que usa hadoop vive al lado del de js')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El que programa en c# vive al lado del que usa cassandra (a la izq)
		try:
			i = self.matriz[2].index('c#')
			if self.matriz[4][i-1] == 'c#':
				print('El que programa en c# vive a la izq del que usa cassandra')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El que usa Neo4J usa sublime
		try:
			i = self.matriz[4].index('neo4j')
			if self.matriz[3][i] == 'sublime':
				print('El que usa neo4j usa sublime')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El ingeniero usa mongo
		try:
			i = self.matriz[1].index('ingeniero')
			if self.matriz[4][i] == 'mongo':
				print('El ingeniero usa mongodb')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		# El desarrollador vive al lado del de la casa azul (a la derecha)
		try:
			i = self.matriz[1].index('desarrollador')
			if self.matriz[1][i+1] == 'desarrollador':
				print('El desarrollador vive al lado del de la casa azul')
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

	########################################################################
	# Quien programa c++ en vim?

		try:
			i = self.matriz[2].index('c++')
			if self.matriz[2][3] == 'vim':
				print('Se encontró la respuesta: El ' + self.matriz[1] +' programa en c+ en vim')
				self.encontrado = True
		except:
			print('Aun no se encuentra la solucion')

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
			encontrado =  self.population[0].encontrado
			self.crossOver(liveness, n_population)
			self.mutate()
			
			if encontrado:
				break
			pass

		self.test()
		print (self.population[0].table)
		print (self.population[0].approve)

	def mutate(self):
		for x in range(0,mutants):
			y = random.randint(0,len(self.population)-1)
			self.population[y].mutate()
			pass
		

	def generate(self, i):
		for x in range(0,i):
			newborn = Tabla()
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
		newborn = Tabla()
		#newborn.randFill()
		for x in range(0,5):
			for y in range(0,5):

				i = random.randint(0,2)
				if i == 0:
					newborn.matriz[x][y] = first.getMatriz(x,y)
				elif i == 1:
					newborn.matriz[x][y] = second.getMatriz(x,y)
				else:
					newborn.matriz[x][y] = third.getMatriz(x,y)
				pass
			pass
		return newborn

	def test(self):
		for x in range(0,len(self.population)):
			self.population[x].test()
			pass

		self.population.sort(key=lambda x: x.puntos, reverse=True)
		for x in range(0,1):
			print (self.population[x].approve)
			pass

puz = Puzzle()
puz.solve()
