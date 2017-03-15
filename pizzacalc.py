class Person(object):

	moneyOwed = 0
	numberOfPizzas = 0

	def __init__(self):
		self.name = self.getName()

	def getName(self):
		return raw_input("Name?: ")
		
	def getcost(self):
		while(True):
			try:
				cost = float(raw_input("Cost?: "))
				break
			except ValueError:
				print ("Please input a numebr: ")
		return cost

	def addPizza(self):
		numberOfPizzas += 1
		return moneyOwed + self.getcost()


nic = Person() 