import random

# Dictionary holding the stages of the hangman figure based on wrong guesses
hangman_art = {
    0: ("   ", "   ", "   "),  # No wrong guesses (initial state)
    1: (" o ", "   ", "   "),  # Head
    2: (" o ", " | ", "   "),  # Head and body
    3: (" o ", "/| ", "   "),  # Head, body, and one arm
    4: (" o ", "/|\\", "   "), # Head, body, and both arms
    5: (" o ", "/|\\", "/  "), # Head, body, both arms, and one leg
    6: (" o ", "/|\\", "/ \\"), # Full hangman (head, body, both arms, both legs)
}

# Tuple of words that the player can guess from
words = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", 
         "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", 
         "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", 
         "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", 
         "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", 
         "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", 
         "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", 
         "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant", 
         "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", 
         "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", 
         "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", 
         "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring", 
         "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", 
         "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", 
         "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", 
         "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", 
         "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", 
         "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", 
         "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", 
         "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", 
         "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", 
         "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", 
         "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros", "rook", 
         "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", 
         "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", 
         "spider", "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", 
         "swallow", "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", 
         "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", 
         "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra")

# Function to display the current hangman figure based on wrong guesses
def display_man(wrong_guesses):
    print("**********")  # Prints a border for the hangman figure
    for line in hangman_art[wrong_guesses]:
        print(line)  # Prints each line of the hangman figure
    print("**********")  # Prints a border after the figure

# Function to display the current hint (progress of the word guessed)
def display_hint(hint):
    print(" ".join(hint))  # Joins the characters with spaces and prints them (e.g. "_ _ _")

# Function to display the final answer when the game ends
def display_answer(answer):
    print(" ".join(answer))  # Joins the answer characters with spaces and prints them

# Main function to run the Hangman game
def main():
    answer = random.choice(words)  # Randomly selects a word from the list
    hint = ["_"] * len(answer)  # Initializes a hint list with underscores for each letter of the answer
    wrong_guesses = 0  # Counter for wrong guesses
    guessed_letters = set()  # Set to store letters that have already been guessed
    is_running = True  # Flag to control the game loop

    # Game loop: runs as long as the game is still ongoing
    while is_running:
        display_man(wrong_guesses)  # Display the hangman based on wrong guesses
        display_hint(hint)  # Display the current state of the hint
        guess = input("Enter a letter: ").lower()  # Prompt the user for a guess and convert it to lowercase

        # Input validation: check if the input is a single letter and if it's alphabetic
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")  # Inform the player if the input is invalid
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"{guess} is already guessed")  # Inform the player if the letter has been guessed already
            continue

        guessed_letters.add(guess)  # Add the guessed letter to the set of guessed letters

        # Check if the guessed letter is in the answer
        if guess in answer:
            # Update the hint to reveal the guessed letter in the correct position(s)
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1  # Increment the wrong guesses counter if the guess is incorrect

        # Check if the player has guessed all the letters correctly (win condition)
        if "_" not in hint:
            display_man(wrong_guesses)  # Display the hangman after the win
            display_answer(answer)  # Display the full answer
            print("YOU WIN!")  # Inform the player they have won
            is_running = False  # End the game loop

        # Check if the player has exceeded the allowed number of wrong guesses (lose condition)
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)  # Display the hangman after the loss
            display_answer(answer)  # Display the full answer
            print("YOU LOSE!")  # Inform the player they have lost
            is_running = False  # End the game loop

# This ensures the main function is called only when the script is run directly
if __name__ == "__main__":
    main()
