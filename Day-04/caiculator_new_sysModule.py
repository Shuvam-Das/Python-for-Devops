import sys
num1 = 10
num2 = 5

def addition():
    add = num1 + num2
    return add

def subtraction():
      sub = num1 - num2
      return sub

def multiplication():
       mul = num1 * num2
       return mul

def division():
       div = num1 / num2
       return div

num1 = sys.argv[1]
operation = sys.argv[2]
num2 = sys.argv[3]

if operation == 'add':
    output = addition(num1, num2)
    print(f"The result of addition is: {output}")
