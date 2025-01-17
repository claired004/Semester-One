#Claire Deng

#init
#Functions
#Adds two numbers and prints result
print("Welcome to Simple Calculator")
def simpleCalc():
    while True:
        print("Please choose an operation")
        print("""1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Quit""")
        option = int(input("1-5: "))
        def add(num1, num2):
            result = num1 + num2
            print(result)
        if option == 1:
            num1 = int(input("please enter the first number: "))
            num2 =  int(input("please enter the second number: "))
            add(num1,num2)
        def subtract(num1, num2):
            result = num1 - num2
        if option == 2:
            num1 = int(input("please enter the first number: "))
            num2 = int(input("please enter the second number: "))
            subtract(num1,num2)
        def multiply(num1, num2):
            result = num1 * num2
            print(result)
        if option == 3:
            num1 = int(input("please enter the first number: "))
            num2 = int(input("please enter the second number: "))
            multiply(num1,num2)
        def divide(num1, num2):
            result = num1/num2
            print(result)
        if option == 4:
            num1 = int(input("please enter the first number: "))
            num2 = int(input("please enter the second number: "))
            divide(num1,num2)
#Main
simpleCalc()


