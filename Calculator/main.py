from math_operations import add, subtract, multiply, divide
from User_input import doMath, getOpperation, getFirstNumber, getNextNumber, getSign

#get the first number 

#get first num from user
fNum = getFirstNumber()
#get the opperation that they want to do
opp = getOpperation()
#print the opperation that they did
print(fNum,getSign(opp))

