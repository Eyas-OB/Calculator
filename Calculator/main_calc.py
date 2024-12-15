from math_operations import add, subtract, multiply, divide
from User_input import doMath, getOpperation, getFirstNumber, getNextNumber

# we want to prompt for the users input consistantly 
# while prompting for the user input we want them to keep putting in numbers
# when they keep putting in numbers then the result will be printed where they will be 
# prompted to keep putting the result in 

fNum = getFirstNumber()

while(True):
    opperation = getOpperation()
    sNum = getNextNumber()
    result = doMath(opperation,fNum,sNum)
    print(result)
    go = input("do you want to keep doing math? press n to stop")
    if(go != "n"):
        while(True):
            opperation = getOpperation()
            sNum = getNextNumber()
            result = doMath(opperation,result,sNum)
            print(result) 
            go = input("do you want to keep doing math? press n to stop")
            if(go == "n"):
                break
                print(result)
    if(go == "n"):
        break
        print(result)
    

