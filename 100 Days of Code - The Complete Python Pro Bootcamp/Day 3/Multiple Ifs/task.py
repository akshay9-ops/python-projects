# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry you have to grow taller before you can ride.")

print('Welcome to the Rollercoaster ride')
height=int(input("Enter your height in cm:"))
bill=0

if height>=200:
    print("Welcome to the Rollercoaster ride, please let us know your age")
    age=int(input("Enter your age: "))
    if age>=18:
        print("Adult ticket is $12")
        bill+=12
    elif age>=12:
        print("Youth ticket is $7")
        bill+=7
    elif age>=45 and age<=55:
        print("Free ride!")
    else:
        print("Child ticket is $5")
        bill+=5
    photo=input("Do you want a photo? Type Yes or No")
    if photo=="Yes":
        bill+=3
        print(f"Your total cost is: {bill}")
        # Add $3 to a bill
    if photo=="No":
        print("Your total cost is: ",bill)
else:
    print("Your height is too short for the ride")