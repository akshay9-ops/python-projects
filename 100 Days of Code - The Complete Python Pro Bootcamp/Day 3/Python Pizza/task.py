print("Welcome to Python Pizza Deliveries!")
S=15
M=20
L=25
bill=0
size = input("What size pizza do you want? S, M or L: ")
if size=="S":
    bill=S
elif size=="M":
    bill=M
elif size=="L":
    bill=L
else:
    print("Wrong input")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni=="Y":
    if size == "S":
        bill+=2
    else:
        bill+=3
elif pepperoni=="N":
    bill


extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese=="Y":
    bill+=1
    print(f"Your final bill is {bill}")
elif extra_cheese=="N":
    bill
    print(f"Your without cheese is {bill}")
