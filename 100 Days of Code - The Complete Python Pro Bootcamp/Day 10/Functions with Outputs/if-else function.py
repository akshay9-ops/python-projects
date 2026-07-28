def format_name(first_name, last_name):
    """Take a first and last name and format it
    to return the title case version for the name"""
    if first_name == "" and last_name == "":
        return "Please enter your first and last name"
    else:
        first_name.title()
        last_name.title()
        output = f"{first_name} {last_name}"
        return output

result =format_name(input("Enter your first name: "), input("Enter your last name: "))
print(result)



i=2100%400
print(i)

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))