from math_operations import add,subtract,multiply,divide

def math(opperation):
    #adding 
    if(opperation == 1): 
        return add(number_user_picked,Second_picked_number)

 # subtracting
    if(opperation == 2):
        return subtract(number_user_picked,Second_picked_number)

#for multply
    if(opperation == 3):
        return multiply(number_user_picked,Second_picked_number)

#for divide
    if(opperation == 4):
        return divide(number_user_picked,Second_picked_number)

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
    


