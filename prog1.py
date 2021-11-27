# Create a program that will ask for grade percentage. 
# Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

def gradepercent():
    global grdpercent
    grdpercent = float(input("Enter grade percentage: "))
    if grdpercent <= 100 and grdpercent >= 96.5: # 97 -100
        print("Mark: 1.00 - Excellent!")
    elif grdpercent < 96.5 and grdpercent >= 93.5: # 94 - 96
        print("Mark: 1.25 - Excellent!")
    elif grdpercent < 93.5 and grdpercent >= 90.5: # 91 - 93
        print("Mark: 1.50 - Very Good!")
    elif grdpercent < 90.5 and grdpercent >= 87.5: # 88 - 90
        print("Mark: 1.75 - Very Good!")
    elif grdpercent < 87.5 and grdpercent >= 84.5: # 85 - 87
        print("Mark: 2.0 - Good")
    elif grdpercent < 84.5 and grdpercent >= 81.5: # 82 - 84
        print("Mark: 2.25 - Good")
    elif grdpercent < 81.5 and grdpercent >= 78.5: # 79 - 81
        print("Mark: 2.50 - Satisfactory")
    elif grdpercent < 78.5 and grdpercent >= 75.5: # 76 - 78
        print("Mark: 2.75 - Satisfactory")
    elif grdpercent <= 75.4 and grdpercent >= 75: # 75 - 75.4
        print("Mark: 3.00 - Passing")
    elif grdpercent < 75 and grdpercent >= 65:
        print ("Mark: 5.00 - Failed")

def display():
    print("-End-")

def grdstatus():
     global grdstatus
     grdstatus = input("Enter grade status (Inc, W, D): ")
     if grdstatus == "Inc":
        print("Your outputs in this subject are INCOMPLETE.")
     elif grdstatus == "W":
        print("Your status in this subject is WITHDRAWN.")
     else: 
        print("Your status in this subject is DROPPED.")

userinput= input("Type [g] to check the equivalent of your grade percent and [s] to check your status in a subject: ")
if userinput == "g":
    gradepercent()
    if grdpercent < 65:
        print("Invalid input. Please enter a valid grade percentage.")
        gradepercent()
    elif grdpercent > 100:
        print("Invalid input. Please enter a valid grade percentage.")
        gradepercent()
else:
    grdstatus()

display()