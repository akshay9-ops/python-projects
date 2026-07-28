#creating function that takes name and converts to proper format
# "Angela Vu"
# My approach
# def format_name():
#     f_name = input("What is your first name: ").lower()
#     l_name = input("What is your last name: ").lower()
#     output = f"{f_name} {l_name}".title()
#     return output
#
# output = format_name()
# print(output)

#Udemy approach

# ---------------------------------------------------
def format_name(f_name, l_name): #Function can take input when its called
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("Angeula","vu"))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

# we can now take the output of function 1 and make input of function 2
output = function_2(function_1("hello"))
print(output)

