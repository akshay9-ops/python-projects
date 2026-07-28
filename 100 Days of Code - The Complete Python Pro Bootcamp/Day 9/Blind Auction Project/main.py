# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)
user_list = {}
more_people = True
while more_people:
        name = input("What is your name? ")
        amount = int(input("How much can you pay? "))
        get_input = input("Do you have more people ").lower()
        if get_input == "yes":
            user_list[name] = amount
            print(user_list)
            print("\n"*100)
        elif get_input == "no":
            user_list[name] = amount
            highest_bid = 0
            winner = ""
            for key in user_list:
                if user_list[key] > highest_bid:
                    highest_bid = user_list[key]
                    winner = key
            # print(highest_bid)
            print(f"{winner} {highest_bid} wins!")
            # print(key)
            more_people = False
            get_input = False
    #compare result

