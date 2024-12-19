from math_operations import add, subtract, multiply, divide
from User_input import doMath, getOpperation, getFirstNumber, getNextNumber, getSign

#get first number
fNum = getFirstNumber()
print(fNum)

opp = getOpperation()

#get next number 
sNum = getNextNumber()

#do the math
result = doMath(opp,fNum,sNum)

print(fNum,getSign(opp),sNum, " = ", result)

go = input("use -1 to stop or hit any key to continue ")

if(go != "-1"):
    while(True): 
        oldResult = result
        print(oldResult)
        opp = getOpperation()
        print(result,getSign(opp))
        nxtNum = getNextNumber()
        result = doMath(opp,result,nxtNum)
        print(oldResult,getSign(opp),nxtNum, " = ", result)
        go2 = input("use -1 to stop or hit any key to continue")
        if(go2 == "-1"):
            break





