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
# who won, computer chose, work
choices=["Rock", "Paper", "Scissors"]
your_choice=input("What are your choices Rock, Paper, Scissors")
computer_choice=random.choice(choices)
print(f"Computer Choice\n {computer_choice}")

# your_choice=input("What do you choose? Type Rock, Paper or Scissors: ").lower()
# computer_choice=("Rock", "Paper", "Scissors")
# print("Computer chose: ", random.choice(computer_choice))

if your_choice=="Rock" and computer_choice=="Paper":
    print(f"Your Choice\n {Rock}")
    print(f"Computer Choice\n {Paper}")
    print("Computer wins!")
elif your_choice=="Rock" and computer_choice=="Scissors":
    print(f"Your Choice\n {Rock}")
    print(f"Computer Choice\n {Scissors}")
    print("You win!")
elif your_choice=="Paper" and computer_choice=="Rock":
    print(f"Your Choice\n {Paper}")
    print(f"Computer Choice\n {Rock}")
    print("You win!")
elif your_choice=="Scissors" and computer_choice=="Paper":
    print(f"Your Choice\n {Scissors}")
    print(f"Computer Choice\n {Paper}")
    print("You win!")
elif your_choice==computer_choice:
    print("Try Again")
