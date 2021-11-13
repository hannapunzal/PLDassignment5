# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number
import time
def inputnumber():
    firstNum = int(input("Enter first number: "))
    secondNum = int(input("Enter second number: "))
    thirdNum = int(input("Enter third number: "))
    if firstNum < secondNum and firstNum < thirdNum:
        print(f"The lowest number among the three is {firstNum}. ")
    elif secondNum < firstNum and secondNum < thirdNum:
        print(f"The lowest number among the three is {secondNum}.")
    else:
        print(f"The lowest number among the three is {thirdNum}.")

inputnumber()
print("-End-")