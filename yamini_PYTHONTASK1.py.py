"Declare and initialize five different variables with distinct data types (e.g., integer, float, string, boolean, list)."
'''s_id = 101
s_cgpa = 8.1
s_name = 'yamini'
is_placed = True
skills = ['python','c','html','sql']
print('s_id is' ,type(s_id))
print('s_cgpa is' ,type(s_cgpa))
print('s_name is' ,type(s_name))
print('is_placed is' ,type(is_placed))
print('skills is', type(skills))'''

"Write a Python function that takes two variables as input, swaps their values, and returns the swapped values."
''' def swap(a,b):
    return b,a
n1 = 10
n2 = 20
print('num1 =', n2)
print('num2 =', n1)'''

"Create a simple calculator program that uses variables to store user input (e.g., numbers and operators) and calculate the result based on the operator."
'''a=int(input())
b=int(input())
op=input('enter operator(+,-,*,/)')
if op == '+':
    res = a+b
elif op == '-':
    res = a-b
elif op == '*':
    res = a*b
elif op == '/':
    if b != 0:
        res = a/b
    else:
        res = 'division by zero is not possible'
else:
    res = 'invalid operator'
print(res) '''

"Use variables to generate a formatted string that includes user-provided information (e.g., name, age, location)."
'''name = 'Yamini'
age = 20
location = 'Hyderabad'
res = f"My name is {name}. I am {age} years old and I live in {location}."
print(res)'''

"Demonstrate the use of variable scope by creating a nested function that accesses and modifies a variable declared in the outer function."
def outer():
    x = 10

    def inner():
        nonlocal x
        x = x + 5
        print("Inside inner:", x)

    inner()
    print("Inside outer:", x)

outer()