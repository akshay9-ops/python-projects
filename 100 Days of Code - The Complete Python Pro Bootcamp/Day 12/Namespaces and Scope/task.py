# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
#
# print(f"enemies outside function: {enemies}")
#
#
# # # Local Scope
# # def drink_potion():
# #     potion_strength = 2
# #     print(potion_strength)
# #
# # drink_potion()
# # print(potion_strength)
#
# # Global Scope
# player_health = 100
#
# # def game():
# #     def drink_potion():
# #         potion_strength = 2
# #         print(player_health)
# #
# # drink_potion()
#
# game_level = 3
# enemies = ["Skeleton","Zombie","Alien"]
#
# def create_enemy():
#     if game_level <5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)
# create_enemy()

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
        return "prime"

print(is_prime(9))