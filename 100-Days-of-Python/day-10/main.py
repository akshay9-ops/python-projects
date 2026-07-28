def add(n1, n2):
    return n1 + n2
# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

#TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using dictionary
from art import logo
#print(operations["*"](4,8))
first_number = int(input("What's the first number?: "))

run_loop = True
while run_loop:
    for operation in operations:
        print(operation)
    pick_operation = input("Pick an operation: ")
    second_number = int(input("What's the next number?: "))
    output_number = operations[pick_operation](first_number, second_number) #2
    output_display = print(f"{first_number} {pick_operation} {second_number} = ", output_number)
    start_loop = input("Type 'y' to continue or 'n' to start a new calculation or x to exit: ").lower()
    if start_loop == "y":
        first_number = output_number #2
        print(first_number)
    if start_loop == "n":
        first_number = int(input("What's the first number?: "))
    if start_loop == "x":
        run_loop = False
