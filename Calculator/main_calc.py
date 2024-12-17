from math_operations import add, subtract, multiply, divide
from User_input import doMath, getOpperation, getFirstNumber, getNextNumber, getSign

# we want to prompt for the users input consistantly 
# while prompting for the user input we want them to keep putting in numbers
# when they keep putting in numbers then the result will be printed where they will be 
# prompted to keep putting the result in 

#gets the first number from the user ex -> 2
fNum = getFirstNumber()

#keeps going until the user asks us to stop
while(True):
    #get the opperation that the user wants to perform ex -> 2 + 
    opperation = getOpperation()
    # print what the user is seeing
    print(fNum,getSign(opperation))
    #gets the next number that they want tho use in the opperation ex -> 2 + 2
    sNum = getNextNumber()
    #evaluates the opperation ex -> 2+2 = 4
    result = doMath(opperation,fNum,sNum)
    #prints the result ex->  4
    print(result)
    #if the user wants to keep putting in numbers they can 
    go = input("do you want to keep doing math? y/n ")
    if(go != "n"):
        while(True):
            print(result)
            #they can do another opperation 
            opperation = getOpperation()
            #print the next opperation
            print(result,getSign(opperation))
            #they can pick the next number that they want to use in the result
            sNum = getNextNumber()
            #do the math with the result and the next number 
            result = doMath(opperation,result,sNum)
            #then the next result will be printed 
            print(result,getSign(opperation))
            #the user will be asked if they want to keep going 
            go = input("do you want to keep doing math? press n to stop ")
            if(go == "n"):
                break
                print(result)
    if(go == "n"):
        break
        print(result)
    

