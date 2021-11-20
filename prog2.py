# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number
import time
def inputnumber():
    firstNum = float(input("Enter first number: "))
    secondNum = float(input("Enter second number: "))
    thirdNum = float(input("Enter third number: "))
    if firstNum < secondNum and firstNum < thirdNum:
        time.sleep(2)
        print(f"The lowest number among the three is {firstNum}. ")
    elif secondNum < firstNum and secondNum < thirdNum:
        time.sleep(2)
        print(f"The lowest number among the three is {secondNum}.")
    else:
        time.sleep(2)
        print(f"The lowest number among the three is {thirdNum}.")

inputnumber()
time.sleep(1)
print("-End-")