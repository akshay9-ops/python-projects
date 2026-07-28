"""We building this class to define
what users can do or not in website"""
class User:
#This function is called every time u create new object from this class
    def __init__(self, user_id, username): # user_id - parameter
        # self.id - attribute associated with class
        self.id = user_id # pass in when any id gets constructed
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","angela")
user_2 = User("002", "mike")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)


# print(user_2.id,user_2.username)
# user_2.id = "002"
# user_2.username = "mike"
#
# print(user_2.id)


"""What if I want to add another object/user with same attributes"""
"""Is there a way to make it simpler?"""

# class Car:
#     def enter_race_mode(self):
#         self.seats = 2
#
# my_car = Car()
# my_car.enter_race_mode()
# print(my_car.seats)