def add(x,y):
    return x+y

def multiply(x,y): 
    return x*y

def divide(x,y):
    
    if(y == 0):
        raise ZeroDivisionError("cant divide by 0")
    else:       
        return x/y

def subtract(x,y):
    return x-y



