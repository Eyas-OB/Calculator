from math_operations import add, subtract, multiply, divide
from User_input import doMath, getOpperation, getFirstNumber, getNextNumber, getSign

#get first number
fNum = getFirstNumber()
print(fNum)

opp = getOpperation()
print(fNum,getSign(opp))

#get next number 
sNum = getNextNumber()
print(fNum,getSign(opp),sNum)

#do the math
result = doMath(opp,fNum,sNum)

print(fNum,getSign(opp),sNum, " = ", result)

go = input("another number? say no to stop")

if(go != "n"):
    while(True): 
        oldResult = result
        print(oldResult)
        opp = getOpperation()
        print(result,getSign(opp))
        nxtNum = getNextNumber()
        result = doMath(opp,result,nxtNum)
        print(oldResult,getSign(opp),nxtNum, " = ", result)




