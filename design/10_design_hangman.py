import random
from collections import defaultdict

# Making secret word - hangman style
alphabets = 'abcdefghijklmnopqrstuvwxyz'
word_length = 5
secret_word = ''.join([random.choice(alphabets) for _ in range(word_length)])
found_positions = [False]*5

# build a map for faster game evaluation
secret_word_desc = defaultdict(list)
def build_word_description():
    for i, char in enumerate(secret_word):
        secret_word_desc[char].append(i)
build_word_description()

# evaluate user inp and progress the game
def evaluate(char, found_alphabets):
    correct_guess = False
    if char in secret_word_desc:
        positions = secret_word_desc[char]
        for position in positions:
            print(position)
            current_word[position] = char
            found_alphabets += 1
            correct_guess = True
            found_positions[position] = True
    return (correct_guess, found_alphabets)

# Give the user a hint
def get_hint():
    for ind, alphabet_found_status in enumerate(found_positions):
        if not alphabet_found_status:
            return secret_word[ind]

if __name__ == "__main__":
    # game state
    is_game_over = False
    was_game_won = False
    remaining_guesses = 6
    remaining_hints = 1
    found_alphabets = 0
    guessed_chars = []
    current_word = ['_ ']*5

    # start game
    while not is_game_over:
        # display
        print("--------------------------------")
        print("Chance# " + str(6 - remaining_guesses + 1) + ", Remaining Chances: " + str(remaining_guesses))
        print("Remaining Hints: " + str(remaining_hints) + ". Enter hint to avail the hint.")
        print(''.join(current_word))
        print("Already Guessed: " + ''.join(guessed_chars))
        
        # accepting input
        correct_input = False
        while not correct_input:
            char = input("Please enter one alphabet: ").lower()
            if len(char) == 4 and char == "hint" and remaining_hints > 0:
                remaining_hints -= 1
                print("Hint: Use " + str(get_hint()))
            elif len(char) == 1 and char.isalpha():
                correct_input = True
        print("--------------------------------", end='\n\n')
        
        # evaluating
        correct_guess, found_alphabets = evaluate(char, found_alphabets)
        guessed_chars.append(char)
        
        # updating game state
        if found_alphabets >= word_length:
            was_game_won = True
            break
        if not correct_guess:
            remaining_guesses -= 1
            if remaining_guesses <= 0:
                is_game_over = True
    
    # result
    if was_game_won:
        print("Congratulations, you correctly guessed: " + secret_word)
    else:
        print("Hard luck! The word was: " + str(secret_word))
