# now ko lang po nalaman na gagawin parin po yung inexample niyo sir sorry po mismong deadline ko lang po nagawa
# Program 3: Life stages
# Create a program that ask for an age of a person
#Display the life stage of the person.
# Rules:
#0 - 12 : Kid
# 13 - 17 : Teen
# 18 : Debut
# 19 above : Adult

def lifeStages():
    global age
    age = float(input("Enter your age: "))
    if age >= 0 and age <= 12:
        print("Life stage: kid")
    elif age > 12 and age <=17:
        print("Life stage: teen")
    elif age == 18:
        print("Life stage: debut")
    else:
        print("Life stage: adult")

lifeStages()
if age < 0:
    print("Invalid input. Please enter your age in years.")
lifeStages()