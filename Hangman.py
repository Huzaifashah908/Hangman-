import random  # Import the random module to choose a random word


# Function to choose a random word from the list
def choose_word():
    words = [  # List of possible words for the game
        "elephant", "butterfly", "chocolate", "mountain", "adventure", "galaxy",
        "ocean", "friendship", "happiness", "whisper", "thunder", "library",
        "pencil", "backpack", "journey", "mirror", "rainbow", "sunflower",
        "diamond", "island", "castle", "history", "fireworks", "treasure",
        "lighthouse", "moonlight", "volcano", "tornado", "waterfall", "penguin",
        "courage", "magic", "paradise", "mystery", "starlight", "compass",
        "universe", "symphony", "gentleman", "nostalgia", "explorer", "breeze",
        "lantern", "fireplace", "carousel", "garden", "voyage", "twilight",
        "buttercup", "horizon", "orchestra", "companion", "fortune", "fountain"
    ]
    return random.choice(words)  # Randomly select and return one word from the list


# Function to display the word with guessed letters revealed and unguessed ones as "_"
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


# Main function to run the Hangman game
def hangman():
    word = choose_word()  # Select a random word for the game
    guessed_letters = set()  # Set to store guessed letters
    attempts = 6  # Number of wrong guesses allowed

    print("Welcome to Hangman!")  # Display welcome message

    while attempts > 0:  # Game loop runs while attempts remain
        print("\nWord:", display_word(word, guessed_letters))  # Show the current state of the word
        print(f"Attempts left: {attempts}")  # Show remaining attempts

        guess = input("Guess a letter: ").lower()  # Get user input and convert to lowercase

        # Validate user input (must be a single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue  # Ask for input again

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue  # Ask for input again

        guessed_letters.add(guess)  # Add the guessed letter to the set

        # Check if the guessed letter is in the word
        if guess in word:
            print("Good job! That letter is in the word.")
        else:
            print("Wrong guess!")
            attempts -= 1  # Reduce the number of attempts for a wrong guess

        # Check if all letters have been guessed correctly
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break  # End the game if the word is fully guessed
    else:
        print("\nGame Over! The word was:", word)  # Display game over message if attempts reach 0


# Run the game when the script is executed
if __name__ == "__main__":
    hangman()

