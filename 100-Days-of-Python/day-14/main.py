import random
from game_data import data

# global variables
random_choice_a = 0 # Current A index
random_choice_b = 0 # Current B index
compare_a = "Compare A"
compare_b = "Against B"
score = 0
name_a = ""
description_a = ""
country_a = ""
followers_a = 0
name_b = ""
description_b = ""
country_b = ""
followers_b = 0

# All functions
# These two functions passes the index within data
def random_choice_function_a():
    global random_choice_a
    random_choice_a = (random.randint(0, len(data)-1))

def random_choice_function_b():
    global random_choice_b
    random_choice_b = (random.randint(0, len(data)-1))
    while random_choice_a == random_choice_b:
        random_choice_b = (random.randint(0, len(data)-1))

# These functions updates each variables within a record
def random_choice_update_function_a():
    global name_a, description_a, country_a, followers_a, compare_a, score
    name_a = (data[random_choice_a]["name"])
    description_a = (data[random_choice_a]["description"])
    country_a = (data[random_choice_a]["country"])
    followers_a = (data[random_choice_a]["follower_count"])

def random_choice_update_function_b():
    global name_b, description_b, country_b, followers_b
    name_b = (data[random_choice_b]["name"])
    description_b = (data[random_choice_b]["description"])
    country_b = (data[random_choice_b]["country"])
    followers_b = (data[random_choice_b]["follower_count"])

# Calling functions
random_choice_function_a()
random_choice_function_b()

random_choice_update_function_a()
random_choice_update_function_b()
# # print output of the random function
# print(f"The random choice is {random_choice_a}")
# print(f"The random choice is {random_choice_b}")

# compare_1 = print(f"{compare_a}: {name_a},a {description_a},from {country_a}")
# compare_2 = print(f"{compare_b}: {name_b},a {description_b},from {country_b}")
# compare_1 = [compare_a, name_a, description_a, country_a]
# compare_2 = [compare_b, name_b, description_b, country_b]

# print(followers_a)
# print(followers_b)

print(f"{compare_a}: {name_a},a {description_a},from {country_a}")
print(f"{compare_b}: {name_b},a {description_b},from {country_b}")
choice = True
while choice:
    your_choice = input("Who has more followers? Type 'A' or 'B':")
    if your_choice =="A" and followers_a > followers_b:
        score += 1
        print(f"You are right, Current score: {score}")
        random_choice_function_b()
        while random_choice_a == random_choice_b:
            random_choice_function_b()
        random_choice_update_function_b()
        print(f"{compare_a}: {name_a},a {description_a},from {country_a}")
        print(f"{compare_b}: {name_b},a {description_b},from {country_b}")
    elif your_choice =="B" and followers_b > followers_a:
        score += 1
        print(f"You are right, Current score: {score}")
        random_choice_a = random_choice_b
        random_choice_update_function_a()
        random_choice_function_b()
        random_choice_update_function_b()
        print(f"{compare_a}: {name_a},a {description_a},from {country_a}")
        print(f"{compare_b}: {name_b},a {description_b},from {country_b}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        choice = False