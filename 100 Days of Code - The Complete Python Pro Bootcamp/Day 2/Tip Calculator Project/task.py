# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))



print("Welcome to the tip calculator")
bill=float(input("What is the total bill? $"))
tip=int(input("What is the tip % you want to pay? 10, 20, 30: "))
people=int(input("How many people to split the bill?"))
split=round((bill/people)+1*(tip/100),2)
print(f"{people} individuals should pay: ${split}")