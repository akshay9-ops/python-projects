import random
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []


def deal_card():
    return random.choice(cards)


start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if start_game == "y":

    player_cards.append(deal_card())
    player_cards.append(deal_card())

    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    player_addition_card = sum(player_cards)
    computer_addition_card = sum(computer_cards)

    continue_game = "y"

    while continue_game == "y" and player_addition_card < 21:

        print(f"Your cards: {player_cards}, current score: {player_addition_card}")
        print(f"Computer's first card: {computer_cards[0]}")

        continue_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if continue_game == "y":
            player_cards.append(deal_card())
            player_addition_card = sum(player_cards)

    # Player busts
    if player_addition_card > 21:
        print(f"Your final hand: {player_cards}, final score: {player_addition_card}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_addition_card}")
        print("Computer wins!")

    else:

        # Computer's turn
        while computer_addition_card < 17:
            computer_cards.append(deal_card())
            computer_addition_card = sum(computer_cards)

        print(f"Your final hand: {player_cards}, final score: {player_addition_card}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_addition_card}")

        # Compare scores
        if computer_addition_card > 21:
            print("Computer went over. You win!")

        elif computer_addition_card > player_addition_card:
            print("Computer wins!")

        elif computer_addition_card < player_addition_card:
            print("You win!")

        else:
            print("It's a draw!")

else:
    print("Thank you for playing!")