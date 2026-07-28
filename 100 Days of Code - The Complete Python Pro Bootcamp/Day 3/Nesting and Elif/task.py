print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster and to know your total fare")
    age=int(input("How old are you? "))
    if age>=18:
        print("Your total fare is $12")
    elif age>=12:
        print("Your total fare is $7")
    else:
        print("Your total fare is $5")
else:
    print("Sorry you have to grow taller before you can ride.")
