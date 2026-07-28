import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list=["Rock","Paper","Scissors"]
user_choice = int(input("Enter your choice? Type 0 for Rock, 1 for paper, 2 for scissors: "))
computer_choice=random.randint(0,2)
print(f"Computer choice: {computer_choice}")

if user_choice==0 and computer_choice ==2:
    print("You won!")
elif computer_choice==0 and user_choice==2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice < computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == user_choice:
    print("Its a draw!")
elif user_choice >=3 or user_choice < 0:
    print("You typed an invalid number. You lose!")