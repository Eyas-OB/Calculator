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
        1: for add
        2: for subtract
        3: for multpuly 
        4: for divide 
        """))
        if(not(opperation > 0 and opperation <= num_opperations)):
            print("this number is out of range")
        else:
            return opperation
    
    
    

def getFirstNumber():
    first = float(input("enter your first number: "))
    return first

def getNextNumber():
    next = float(input("enter the next number: "))

