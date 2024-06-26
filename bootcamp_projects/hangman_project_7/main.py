# DAY 7 - Hangman Project
import random
from replit import clear
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list 

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo) 

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    clear() # Clears console when user guesses letter
    
    if guess in display:
        print(f"You've already guessed the letter {guess}.")
 
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"'{guess}' is not in the word. You have lost a life :(")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"The answer was {chosen_word}. You lose!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])