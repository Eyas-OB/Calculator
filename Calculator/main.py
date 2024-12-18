from math_operations import add, subtract, multiply, divide
from User_input import doMath, getOpperation, getFirstNumber, getNextNumber, getSign

#get first number
fNum = getFirstNumber()
print(fNum)

while(True):
    opp = getOpperation()
    print(fNum,getSign(opp))

    #get next number 
    sNum = getNextNumber()
    print(fNum,getSign(opp),sNum)

    #do the math
    result = doMath(opp,fNum,sNum)

    print(fNum,getSign(opp),sNum, " = ", result)



