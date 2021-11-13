# Create a program that will ask for grade percentage. 
# Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

def gradepercent():
    global grdpercent
    grdpercent = int(input("Enter grade percentage: "))
    if grdpercent <= 100 and grdpercent >= 97:
        print("Mark: 1.00 - Excellent!")
    elif grdpercent < 97 and grdpercent >= 94:
        print("Mark: 1.25 - Excellent!")
    elif grdpercent < 94 and grdpercent >= 91:
        print("Mark: 1.50 - Very Good!")
    elif grdpercent < 91 and grdpercent >= 88:
        print("Mark: 1.75 - Very Good!")
    elif grdpercent < 88 and grdpercent >= 85:
        print("Mark: 2.0 - Good")
    elif grdpercent < 85 and grdpercent >= 82:
        print("Mark: 2.25 - Good")
    elif grdpercent < 82 and grdpercent >= 79:
        print("Mark: 2.50 - Satisfactory")
    elif grdpercent < 79 and grdpercent >= 76:
        print("Mark: 2.75 - Satisfactory")
    elif grdpercent == 75:
        print("Mark: 3.00 - Passing")
    elif grdpercent < 75 and grdpercent >= 65:
        print ("Mark: 5.00 - Failed")

def display():
    print("-End-")

gradepercent()
display()