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

		##########################################################
		#The Englishman lives in the red house.
		try:
			i = self.matriz[1].index('Englishman')
			if self.matriz[0][i] == 'red':
				#print('The Englishman lives in the red house.')
				self.puntos += 1	
				self.approve +=1
			else:
					self.puntos -= fail_score
		except:
			self.puntos -= punish_score


		#The Swede keeps dogs.
		try:
			i = self.matriz[1].index('Swede')
			if self.matriz[3][i] == 'dogs':
				#print('The Swede keeps dogs')
				self.puntos += 1	
				self.approve +=1
			else:
					self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The Dane drinks tea.
		try:
			i = self.matriz[1].index('Dane')
			if self.matriz[4][i] == 'tea':
				#print('The Dane drinks tea')
				self.puntos += 1	
				self.approve +=1
			else:
					self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The green house is just to the left of the white one.
		try:
			i = self.matriz[0].index('green')
			if self.matriz[0][i+1] == 'white':
				#print('The green house is just to the left of the white one.')
				self.puntos += 1	
				self.approve +=1
			else:
					self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The owner of the green house drinks coffee.
		try:
			i = self.matriz[0].index('green')
			if self.matriz[4][i] == 'coffee':
				#print('The owner of the green house drinks coffee.')
				self.puntos += 1	
				self.approve +=1
			else:
					self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The Pall Mall smoker keeps birds.
		try:
			i = self.matriz[2].index('Pall Mall')
			if self.matriz[3][i] == 'birds':
				#print('The Pall Mall smoker keeps birds.')
				self.puntos += 1	
				self.approve +=1
			else:
					self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The owner of the yellow house smokes Dunhills.
		try:
			i = self.matriz[0].index('yellow')
			if self.matriz[2][i] == 'Dunhills':
				#print('The owner of the yellow house smokes Dunhills.')
				self.puntos += 1	
				self.approve +=1
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The man in the center house drinks milk.
		try:
			if self.matriz[4][2] == 'milk':
				#print('The man in the center house drinks milk.')
				self.puntos += 1	
				self.approve +=1
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The Norwegian lives in the first house.
		try:
			if self.matriz[1][0] == 'Norwegian':
				#print('The Norwegian lives in the first house.')
				self.puntos += 1	
				self.approve +=1
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The Blend smoker has a neighbor who keeps cats.
		try:
			i = self.matriz[2].index('Blend')
			if i==0:
				if self.matriz[3][i+1] == 'cats':
					#print('The Blend smoker has a neighbor who keeps cats.')
					self.puntos += 1
					self.approve +=1
				else:
					self.puntos -= fail_score
			elif i==4:
				if self.matriz[3][i-1] == 'cats':
					#print('The Blend smoker has a neighbor who keeps cats.')
					self.puntos += 1
					self.approve +=1
				else:
					self.puntos -= fail_score
			else:
				if self.matriz[3][i+1] == 'cats' or self.matriz[3][i-1] == 'cats':
					#print('The Blend smoker has a neighbor who keeps cats.')
					self.puntos += 1
					self.approve +=1
				else:
					self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The man who smokes Blue Masters drinks bier.
		try:
			i = self.matriz[2].index('Blue Masters')
			if self.matriz[4][i] == 'bier':
				#print('The man who smokes Blue Masters drinks bier.')
				self.puntos += 1	
				self.approve +=1
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The man who keeps horses lives next to the Dunhill smoker.
		try:
			i = self.matriz[3].index('horse')
			if self.matriz[2][i-1] == 'Dunhills':
				#print('The man who keeps horses lives next to the Dunhill smoker.')
				self.puntos += 1	
				self.approve +=1
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The German smokes Prince.
		try:
			i = self.matriz[1].index('German')
			if self.matriz[2][i] == 'Prince':
				#print('The German smokes Prince.')
				self.puntos += 1	
				self.approve +=1
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#The Norwegian lives next to the blue house.
		try:
			i = self.matriz[1].index('Norwegian')
			if self.matriz[0][i+1] == 'blue':
				#print('The Norwegian lives next to the blue house.')
				self.puntos += 1	
				self.approve +=1
			else:
				self.puntos -= fail_score
		except:
			self.puntos -= punish_score

		#print(self.table)
		#print(self.score)

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
			

			if approve >= 14:
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
					newborn.matriz[x][y] = first.getTable(x,y)
				elif i == 1:
					newborn.matriz[x][y] = second.getTable(x,y)
				else:
					newborn.matriz[x][y] = third.getTable(x,y)
				pass
			pass
		return newborn

	def test(self):
		for x in range(0,len(self.population)):
			self.population[x].test()
			pass

		self.population.sort(key=lambda x: x.score, reverse=True)
		for x in range(0,1):
			print (self.population[x].approve)
			pass


puz = Puzzle()
puz.solve()
