# Number Mystery

Project Dates

	•	Started: April 26, 2023
	•	Finished: April 29, 2023

Description

Number Mystery is a fun and interactive number-guessing game created in Python. Players select a difficulty level, then attempt to guess a randomly generated number within a limited number of tries. The game provides hints along the way, making it challenging yet enjoyable for players of all skill levels.

Features

	•	Difficulty Levels: Choose between three levels:
	•	Easy: Guess a number between 1 and 10 with 3 attempts.
	•	Medium: Guess a number between 1 and 50 with 5 attempts.
	•	Hard: Guess a number between 1 and 100 with 7 attempts.
	•	Hints: After each incorrect guess, hints indicate if the guessed number is too high or too low.
	•	Error Handling: Handles invalid inputs gracefully, preventing crashes due to unexpected entries.
	•	Replay Option: After finishing a round, players can choose to play again or exit the game.

How to Play

	1.	Select a Difficulty Level: Run the game, then select a difficulty level by entering a number:
	•	1: Easy (1-10)
	•	2: Medium (1-50)
	•	3: Hard (1-100)
	•	4: Quit (Exit the game)

	2: Guess the Number: The game prompts you to guess a number within the range for the selected difficulty.
	3.	Receive Feedback: After each guess, the game provides feedback:
		•	“Too low” if your guess is less than the target number.
	 •	“Too high” if your guess is greater than the target number.
	4.	Win or Lose: If you guess the correct number within the allowed attempts, you win! If you use up all attempts, the correct number is revealed, and the game ends.

Installation

	1.	Clone the repository:

git clone https://github.com/TechVoyager/Number-Mystery.git


	2.	Navigate to the project directory:

cd Number-Mystery


	3.	Run the game:

python number_mystery.py



Requirements

	•	Python: Version 3.6 or higher
	•	Modules: No additional modules required; uses only Python’s built-in random module

Code Structure

	•	menu(): Handles the game menu and difficulty selection.
	•	game(min_num, max_num, max_guesses): Runs the main game logic, generating a random number and tracking player guesses.
	•	Error Handling: Ensures invalid inputs don’t interrupt gameplay.

Example Gameplay

Welcome to Mysterious Number!
1. Easy (1-10)
2. Medium (1-50)
3. Hard (1-100)
4. Quit
==][====================================][==
Enter your choice (1-4): 2

Guess a number between 1 and 50: 25
Too low, try again.

Guess a number between 1 and 50: 37
Congratulations, you guessed the number in 2 guesses!

Future Improvements

	•	Add more difficulty levels or customizable ranges
	•	Multiplayer mode: Take turns guessing with friends
	•	Score tracking: Keep track of wins and guesses over multiple rounds

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

License

This project is licensed under the MIT License.

Author

	•	Name: Xaiver Hickey
	•	GitHub: TechVoyager

This updated version should display correctly on GitHub, with proper formatting for lists and code blocks. Let me know if you need further adjustments!