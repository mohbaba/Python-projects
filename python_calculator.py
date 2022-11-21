

def add(a,b):
    result = a + b
    return 'Sum: ', result 

def subtract(a,b):
    result = a - b
    return 'Result: ' , result

def multiply(*numbers):
    result = 1
    for num in numbers:
        result = result * num 
        
    print('Product: ' , result) 

def division(a,b):
    result = a / b
    print('Result: ', result)

def square(a):
    result = a **2 
    print('Square: ', result)
    
def square_root(a):
    result = a **( 1/2)
    print('Square root = ', result)
    
def cube_root(a):
    result = a ** (1/3)
    print('Cube root = ', result)

def quadratic_eqn(a,b,c):
    root_value = b **2 - (4 * a * c)
    divisor = 2 * a 
    s = square_root(root_value)
    x1 = - b + s / divisor
    # x2 = (-b  - square_root(root_value)) / divisor
    
    
    # print('x = ', x1 , 'or', x2 )

division(6,2)
# square_root(4)  
# quadratic_eqn(5,6,1)
# multiply(2,5,2)

