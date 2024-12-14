def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def divide(x,y):
    return x/y

def subtract(x,y):
    return x-y

def ask_user(): 
    choice = float(input("""
    welcome to my calculator what would you like to do?
    1 for add 
    2 for multiply 
    3 for divide 
    4 for subtract 
    """))  
    return choice

value = ask_user()

while(value <= 0 or value >= 5):
    if(value <= 0 or value >= 5):
        print("value was not 1-4 try again")
    value = ask_user()


first_number = float(input("pick your first number "))
Second_number = float(input("pick your second number "))



if(value == 1):
   result = add(first_number,Second_number)

if(value == 2):
    result = mul(first_number,Second_number)

if(value == 3):
    result = divide(first_number,Second_number)

if(value == 4):
    result = subtract(first_number,Second_number)


print(result)

