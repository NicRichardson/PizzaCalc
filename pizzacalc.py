from Person import Person

def TryExcept(varType, message, output, returnVal):
    while True:
        try:
            returnVal = varType(input(message))
            break
        except ValueError:
            print(output)
    return returnVal

def calcTotalCost(people, tax):
    totalCost = 0
    tip = 0
    while(True):
        try:
            tipType = str(input("Tip percentage (T) or Tip amount (A)?: "))
            if(tipType.lower() != "t" and tipType.lower() != "a"):
                int("This line forces an error")
            break
        except ValueError:
            print ("Please input valid option")

    if(tipType.lower == "t"):
        tip = TryExcept(float, "What percentage do you want to tip?: ", "Please input a number", tip)
        
    else: 
        tip = TryExcept(float, "What amount would you want to tip?: ", "Please input a number: ", tip)
        
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