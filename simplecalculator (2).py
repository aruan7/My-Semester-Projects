#Simple Calculator

#Init

#Functions
def add(num1, num2):
    result = int(num1) + int(num2)
    print(result)
def subtract(num1, num2):
    result = int(num1) - int(num2)
    print(result)
def multiply(num1, num2):
    result = int(num1) * int(num2)
    print(result)
def divide(num1, num2):
    result = int(num1)/int(num2)
    print(result)

def simplecalculator():
    print("Welcome to simple calculator")
print("Please select an operation: " )
print("""1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit""")
operation = int(input("(1-5) Option: "))
if operation == 1:
    int1 = input("Enter the first number: ")
    int2 = input("Enter the second number: ")
    add(int1, int2)
elif operation == 2:
    int1 = input("Enter the first number: ")
    int2 = input("Enter the second number: ")
    subtract (int1, int2)
elif operation == 3:
    int1 = input("Enter the first number: ")
    int2 = input("Enter the second number: ")
    multiply (int1, int2)
elif operation == 4:
    int1 = input("Enter the first number: ")
    int2 = input("Enter the second number: ")
    divide (int1, int2)
elif operation == 5:
    while True:
        break

#Main
simplecalculator()



