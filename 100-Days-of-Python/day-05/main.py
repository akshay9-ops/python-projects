import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level
password_list = []
for char in range(0, nr_letters):
    # 1 to 4
    random_char = random.choice(letters)
    password_list += random_char
    #print(password_list)            this is only to check

# for symbols
for symb in range(0,nr_symbols):
    password_list+=random.choice(symbols)
    #print(password_list)            this is only to check

# for numbers
for num in range(0,nr_numbers):
    password_list+= random.choice(numbers)
    #print(password_list)            #this is only to check

random.shuffle(password_list)
print(password_list)

password =""
for pwd in password_list:
    password += pwd
print(password)




# Easy Level
# password=""
# # Let's assume letter=4
# for char in range(0, nr_letters):
#     # 1 to 4
#     random_char = random.choice(letters)
#     password += random_char     password = passwprd + random_char
#     #print(password)            this is only to check
#
# # for symbols
# for symb in range(0,nr_symbols):
#     password+=random.choice(symbols)
#     #print(password)            this is only to check
#
# # for numbers
# for num in range(0,nr_numbers):
#     password+= random.choice(numbers)
    #print(password)            this is only to check

# print(password)