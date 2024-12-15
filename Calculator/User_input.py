from math_operations import add,subtract,multiply,divide

def doMath(opperation,x,y):
    #adding 
    if(opperation == 1): 
        return add(x,y)

 # subtracting
    if(opperation == 2):
        return subtract(x,y)

#for multply
    if(opperation == 3):
        return multiply(x,y)

#for divide
    if(opperation == 4):
        return divide(x,y)

#counts number of opperations 
num_opperations = 4

def getOpperation():
    while(True):
        opperation = float(input("""
        What would you like to do? 
        1: +
        2: -
        3: * 
        4: / 
        """))
        if(not(opperation > 0 and opperation <= num_opperations)):
            print("\t",opperation,"is is out of range")
        else:
            return opperation

def getSign(x):
    if(x == 1): 
        return "+"

 # subtracting
    if(x == 2):
        return "-"

#for multply
    if(x == 3):
        return "*"

#for divide
    if(x == 4):
        return "/"


def getFirstNumber():
    first = float(input("enter your first number: "))
    return first

def getNextNumber():
    nextNum = float(input("enter the next number: "))
    return nextNum

