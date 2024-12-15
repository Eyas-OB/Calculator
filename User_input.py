#I want to be able to ask for the users input I want them to be able to put 
#a fuck ton of numbers in while we keep doing opperations and only when the users 
#want to stop putting numbers in then we can say stop

#we can do somthing like this 
# what do you want to do 

#1 : add
#2 : multply
#3 : Subtract
#4 : Divide 

# then after they say what they want to do we ask for the first 2 numbers 
# after that the user will be able to keep inputing the next number 

#lets ask the user what the want to do 
from math_operations import add,subtract,multiply,divide

def math(opperation):
    if(opperation == 1): 
        return add(number_user_picked,Second_picked_number)

#if the user wants to subtract
    if(opperation == 2):
        return subtract(number_user_picked,Second_picked_number)

#for multply
    if(opperation == 3):
        return multiply(number_user_picked,Second_picked_number)

#for divide
    if(opperation == 4):
        return divide(number_user_picked,Second_picked_number)

number_user_picked = float(input("pick your first number: "))

# now we want the user to pick the next number to do the opperation on 
#I am going to make a varable called options because we can always add more math opperations
#later 

num_opperations = 4



opperation = float(input("""
What would you like to do?
1: for add
2: for subtract
3: for multpuly 
4: for divide 
"""))

#they need to pick somthing larger than 0
#and less than or eaqual to the number of opperations 
while(not(opperation > 0 and opperation <= num_opperations)):
    opperation = float(input("""
    That is not a valid number please try again 

    What would you like to do? 
    1: for add
    2: for subtract
    3: for multpuly 
    4: for divide 
    """))

#if the user picks somthing that actually exists then we want them to be able to change some numbers
# for example if they picked a number and then they picked an opperation lets have them pick another 
# number 

Second_picked_number = float(input("pick another number"))

#now that the user picked 2 numbers they can do a calculation 

result = math(opperation)

print(result)

#so now we can store the math opperation in a function but we should try to get the user input and store
#that in a function 