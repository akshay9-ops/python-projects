#
# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return "Not prime"
#     return "Prime"
#
#
# print(is_prime(19))
#
# remainder = num % i
# if remainder % i == 0:
#     print("is not prime")
#     final_output = "not prime"
# else:
#     print("prime")
#     final_output = "prime"
# return final_output

# num = 12
#
# for i in range(2, num):
#
#     print(f"{num} % {i} = {num % i}")

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
print(is_prime(9))