#Step 5

import random
import hangman_words
import hangman_art

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
print("Welcome to Hangman", hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guesssed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guesssed_letters:
        print(f"You've already guessed {guess}")
    else:
        guesssed_letters.append(guess)

    #Check guessed letter
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"The letter {guess} is not in the word. You lose a life.")
        lives -= 1

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if lives == 0:
        end_of_game = True
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])

if lives == 0:
    print("You lose.")
    print(f"The word was {chosen_word}")
