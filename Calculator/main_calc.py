from math_operations import add, subtract, multiply, divide
from User_input import doMath, getOpperation, getFirstNumber, getNextNumber

# we want to prompt for the users input consistantly 
# while prompting for the user input we want them to keep putting in numbers
# when they keep putting in numbers then the result will be printed where they will be 
# prompted to keep putting the result in 


firstNumber = getFirstNumber()

while(True):
    #get the opperation that they wish to perform 
    opperation = getOpperation()
    nextNum = getNextNumber()
    result = doMath(opperation,firstNumber,nextNum)
    print(result)
    going = input("more math? say no to stop")
    if(going == no):
        break
