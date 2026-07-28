# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount):
    if direction == 'encode':
        encrypt(original_text, shift_amount)
    if direction == 'decode':
        decrypt(original_text, shift_amount)


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        if letter not in alphabet:
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")


def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        if letter not in alphabet:
            cipher_text += letter
    print(f"Here is the decoded result: {cipher_text}")

play_game = True

while play_game:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2: What happens if the user enters a number/symbol/space?




    # TODO-3: Can you figure out a way to restart the cipher program?

    caesar(original_text=text, shift_amount=shift)
    play_game = input("Want to play again? Yes or no").lower()
    if play_game == "yes":
        play_game = True
    else:
        play_game = False




