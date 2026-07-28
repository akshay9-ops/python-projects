import random

random_number = random.choice(range(1,100))
print(f"Pssss: {random_number}")
hard_attempt = 5
easy_attempt = 10
attempt = ""
guess = ""
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
game_mode=input("Choose a difficulty level: 'easy' or 'hard': ")
if game_mode == "easy":
    attempt = easy_attempt
    print("You have 10 attempts remaining to guess the number.")
elif game_mode == "hard":
    attempt = hard_attempt
    print("You have 5 attempts remaining to guess the number.")
else:
    print("Enter a valid option")
print(attempt)
def game(random_number,attempt):
    while attempt > 0:
        guess = int(input("Guess a number: "))
        if guess > random_number:
            attempt -= 1
            print("Too high!")
            print(f"You have {attempt} attempts remaining to guess the number.")
        elif guess < random_number:
            attempt -= 1
            print("Too low!")
            print(f"You have {attempt} attempts remaining to guess the number.")
        elif guess == random_number:
            print("Congratulations! You guessed the number!")
            return
    print("Game Over! You lost all attempts!")
game(random_number,attempt)




