class Person(object):
    moneyOwed = 0
    def __init__(self):
        self.name = self.getName()

    def getName(self):
        return input("Name?: ")
        
    def getcost(self):
        while(True):
            try:
                cost = float(input("Cost?: "))
                break
            except ValueError:
                print ("Please input a number: ")
        return cost

    def addPizza(self):
        self.moneyOwed += self.getcost()
        return self.moneyOwed