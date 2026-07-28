import random

# random_integer=random.randint(1,10)
# print(random_integer)
#
# # random_number = random.random() * 10
# # print(random_number)
#
# random_float = random.uniform(0.0,10.0)
# print(random_float)

#prints heads or tails -> depend on random number u generate
random_number=random.randint(1,2)
if random_number == 1:
    print("Heads")
else:
    print("Tails")