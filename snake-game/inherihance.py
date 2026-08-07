# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale.")
#
#
# class Fish(Animal):
#     def __init__(self):
#         #initialize call to the super class and initializer
#         super().__init__()
#
#     def swim(self):
#         print("swim in water ")
#
# # Modify method of super/parent class
#     def breathe(self):
#         super().breathe()
#         print("doing this under water")
#
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)

# class Dog:
#     def __init__(self):
#         self.temperament = "loyal"
#
#     def bark(self):
#         print("bark")
#
# class labrador:
#     def __init__(self):
#         self.temperament = "labrador"
#
# mike = labrador()
# print(mike.temperament)

piano_keys = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")

print(piano_keys[::-1])