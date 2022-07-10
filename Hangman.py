import random

# Open .txt file containing common english nouns and save words in a hangman list
words_list = []
hangman_words = []
with open('words.txt') as f_obj:
    contents = f_obj.readlines()

for line in contents:
    words_list.append(line)

for word in words_list:
    hangman_words.append(word.strip())

# Have the computer pick a random word from the list
computer_word = hangman_words[random.randint(0,len(hangman_words))]

play = input("Would you like to play hangman? Y/N ")

# Do you want to play Hangman?
while True:
    if play.upper() == 'Y':
        print("Okay, I will pick a word...")
        break
    elif play.upper() == 'N':
        print("Maybe another time.")
        quit()
    else:
        print("Invalid Response. Please type 'Y' or 'N' next time.")
        play = input("\nWould you like to play hangman? Y/N ")

# Actual game
allowable_guesses = 5
num_of_letters = len(computer_word)
print(f"I have selected a word that contains {num_of_letters} letters. You have {allowable_guesses} guesses.")

board = ''
for i in range(0,len(computer_word)):
    board += '_ '
print(board)

used_guesses = []
updated_board = []
for i in range(0,len(computer_word)):
    updated_board.append('_ ')

while allowable_guesses > 0:
    print(f"You have already guessed: {used_guesses}\n")
    guess = input("Please guess a letter: ")

    # Check to see if the guess has already been made
    if guess.lower() in used_guesses:
        print(f"You have already guessed '{guess.lower()}'. Please guess again.")
        continue

    used_guesses.append(guess.lower())

    # If the guess is in the word
    if guess.lower() in computer_word:
        if computer_word.count(guess.lower()) == 1:
            print(f"There is {computer_word.count(guess.lower())} '{guess}' ")
        if computer_word.count(guess.lower()) > 1:
            print(f"There are {computer_word.count(guess.lower())} '{guess}' ")


        # Find indexes of the letters in the word
        indexes = []
        for i in range(0,len(computer_word)):
            if computer_word[i] == guess.lower():
                indexes.append(i)

        # Update the board to reflect the guesses made
        for i in range(0, len(computer_word)):
            if indexes.count(i) == 1:
                updated_board[i] = guess.lower()

        # Convert the updated board to a string
        board = ''
        for letter in updated_board:
            board += ' ' + letter

    # Calculate how many guesses you have left
    if guess.lower() not in computer_word:
        allowable_guesses += -1

    print(board)

    # Check to see if you won
    if '_ ' not in updated_board:
        print(f"You win! The word was {computer_word}.")
        quit()

    if allowable_guesses > 1:
        print(f"You have {allowable_guesses} guesses left.")
    if allowable_guesses == 1:
        print(f"You have {allowable_guesses} guess left.")

# You lose
print(f"Sorry you have no more guesses. The word was '{computer_word}'.")










