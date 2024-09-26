# Date: 04 - 26 - 2023
# Finished: 04 - 29 - 2023
# Name: Xaiver Hickey
# Project Name: Number Mystery 


import random

# Game Menu
def menu():
    play_again = True

    # Difficulty scale.
    while play_again:
        print("Welcome to Mysterious Number!")
        print("1. Easy (1-10)")
        print("2. Medium (1-50)")
        print("3. Hard (1-100)")
        print("4. Quit")
        print("==][====================================][==")
        choice = input("Enter your choice (1-4): ")

        # game(1, 10, 3) 1 is the starting number, and 10, 50, 100 is the maximum number. 
        # 3, 5, 7 is the number of guesses allowed. 
        if choice == "1":
            game(1, 10, 3)
        elif choice == "2":
            game(1, 50, 5)
        elif choice == "3":
            game(1, 100, 7)

        # Reply with 4 to break loop. 
        elif choice == "4":
            play_again = False
            print("Thanks for playing!")
        
        # Fail safe error to help user not to break the application.
        else:
            print("Invalid choice. Try again.")

# Main Game Function
def game(min_num, max_num, max_guesses):
    num = random.randint(min_num, max_num)
    num_guesses = 0

    # Loop function. 
    while num_guesses < max_guesses:

        try: # Informs the player the two num. The var changes based on difficulty.
            guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
            num_guesses += 1

            if guess < num: # This gives player a hint if the num too low. Subtract -1 guess
                print("Too low, try again.")

            elif guess > num: # This gives player a hint if the num too high. Subtract -1 guess
                print("Too high, try again.")

            else: # This rewards the player with a victory. Informing how many guesses it took.
                print(f"Congratulations, you guessed the number in {num_guesses} guesses!")
                return # Return to menu
            
        # Fail safe incase invalid input won't break it.
        except ValueError: 
            print("Invalid input. Try again.")

    print("===][=========================================][===")
    print(f"Game Over... The number was {num}.")

if __name__ == "__main__":
    menu()
