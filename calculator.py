def add_numbers(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a*b

def division (a,b):
    if b == 0:
        print("Error: A number is not divisible by zero!")
    else:
        return a/b

def calculator():
    print("Welcome to the calculator!")
    print("Select the action you want to perform.")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice=int(input("Make your choice (1/2/3/4): "))

    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))

    if choice== 1:
        print("Answer: ", add_numbers(num1,num2))
    elif choice== 2:
        print("Answer: ", subtraction(num1,num2))
    elif choice== 3:
        print("Answer: ", multiplication(num1, num2))
    elif choice== 4:
        print("Answer: ", division(num1,num2))
    else:
        print("You entered an invalid number!")

calculator()