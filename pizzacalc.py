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


def calcTotalCost(people, tax):
    totalCost = 0
    while(True):
        try:
            tipType = str(input("Tip percentage (T) or Tip amount (A)?: "))
            if(tipType.lower() != "t" and tipType.lower() != "a"):
                int("This line forces an error")
            break
        except ValueError:
            print ("Please input valid option")

    if(tipType.lower == "t"):
        while(True):
            try:
                tip = float(input("What percentage do you want to tip?: "))
                break
            except ValueError:
                print("Please input a number")
    else: 
        while(True):
            try:
                tip = float(input("What amount would you want to tip?: "))
                break
            except ValueError:
                print("Please input a number: ")

    if(tipType == "t"):
        for person in people:
            totalCost += person.moneyOwed
        totalCost *= (1+(tip/100))

    else:
        for person in people:
            totalCost += person.moneyOwed
        totalCost += tip

    totalCost *= (1+(tax/100))

    return totalCost



