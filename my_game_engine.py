#A Simple text-based Tic-Tac-Toe game (for now)

#Created 2021/08/08
#Last updated 2021/08/10

#PLANNED CHANGES:
#	- Give player the option to quit every time they are called to input information.
#	- Compile all comparison tests into a module for simplicity.
#	- Use time module to make the gameplay a bit smoother.
#	- Add rounds & a scorekeeping system. Allow player to choose the amount of rounds they can play.
#	- Smarten up the AI by creating a module of comparison tests for the Tic-Tac-Toe game. Selection of specific comparison tests can be used to scale the AI's "difficulty".
#	- Add offline multiplayer (basically make it so more than one person can play the games).
#	- Allow the user to select how large they'd like the Tic-Tac-Toe board to be. This is probably possible with a module of expansion strings & logic that can be appended to the game's respective attributes.
#	- Add more games via more classes.
#	- Add a GUI via Tkinter (still gotta learn how that works tho).

#Comments with an exclamation mark (!) denote ideas and/or reminders.

#README - This program is more or less a pathfinder/experiment where I tried applying as many concepts as I could in favor of simplicity. That doesn't mean I won't try to simplify it as time goes on. I do, however, appreciate as much criticism as I can get. Have at it.

import sys
import random

def main():
	"""Gives user main selection choices & calls what is needed. Manages flow, establishes necessary global variables."""
	firstPlayerName = str(input("Enter your username:\n\t</> "))
	print(F"Welcome, {firstPlayerName.title()}!")
	gameChoice = str(input("ENTER NAME OF GAME TO PLAY (tictactoe for tictactoe): "))
	if gameChoice.lower() == "tictactoe":
		tictactoe = TicTacToe(firstPlayerName)
		tictactoe.tic_tac_toe()

class TicTacToe:
	"""All objects, attributes, and methods pertaining to the Tic-Tac-Toe game."""
	def __init__(self, player_name, name="big boi"):
		"""Initialize all data for the Tic-Tac-Toe game."""
		self.artificialPlayerName = name
		self.playerName = player_name
		self.playerSymbol = ""
		self.artificialPlayerSymbol = ""
		self.choice = ""
		self.quit = False
		self.gameBoard = { #The game board. This is the heart of the game, a simple 9-entry dictionary. Nice.
		"a3": " ", "b3": " ", "c3": " ",
		"a2": " ", "b2": " ", "c2": " ",
		"a1": " ", "b1": " ", "c1": " "}

		#The game board in a displayable format. Is redefined right before it is printed to ensure that no data is left out.
		self.gameBoardDisplay = ""

	def print_board(self):
		"""Displays game board with all relevant information."""
		print(self.gameBoardDisplay)

	def player_symbol_selection(self):
		"""Ask's for player's symbol selection."""
		while True: #Asks for user's symbol & gives option to quit.
			userChoice = str(input("\nSELECT LETTER FOR GAME: o / x \n'q' - Quit program.  \n\t</> "))
			if userChoice.upper() == "O" or userChoice.upper() == "X":
				self.playerSymbol = userChoice.upper()
				break
			elif userChoice.lower() == "q":
				sys.exit()
			else:
				print(F"'{userChoice}' is invalid input. Please type 'o' or 'x'.\n")

	def artificial_player_symbol_selection(self): 
		"""Selects artificial player's tic tac toe symbol based on first user's symbol selection."""
		if self.playerSymbol.upper() == "X":
			self.artificialPlayerSymbol = "O"
		elif self.playerSymbol.upper() == "O":
			self.artificialPlayerSymbol = "X"
		else:
			print("artificial_symbol_select function ERROR")

	def player_choice(self):
		"""Player selects which to occupy on board."""
		while True:
			userChoice = input(str(F'\nEnter letter of column followed by number of row of spot that you would like to occupy. Enter q to quit.\n\t</> '))
			if userChoice.lower() == "q": #Give player choice to quit the game at any time.
				sys.exit()
			elif userChoice in self.gameBoard.keys(): 
				if self.gameBoard[userChoice] == " ":
					self.choice = userChoice
					print(F"{self.playerName.title()} chose {self.choice}")
					break
				elif self.gameBoard[userChoice] != " ":
					print(F"{userChoice} has already been chosen. Please choose again.")
			else:
				print(F"'{userChoice}' is invalid input. For example, 'a3' defines the top left spot & c1 defines the bottom right spot.")

		self.gameBoard[self.choice] = self.playerSymbol

	def artificial_player_choice(self): 
		"""Gives a random tic tac toe answer by compiling all empty spaces into a list & then randomly selecting one."""
		validOptions = []
		for key, value in self.gameBoard.items():
			if value == ' ':
				validOptions.append(key)

		self.choice = validOptions[random.randrange(0, len(validOptions))]
		print(F"{self.artificialPlayerName.title()} chose spot {str(self.choice)}.")
		self.gameBoard[self.choice] = self.artificialPlayerSymbol

	def determine_victor(self):
		"""Comparison algorithm to determine victor."""

		#Update the game board display
		self.gameBoardDisplay = F"\t\n\t3 {str(self.gameBoard['a3'])} | {str(self.gameBoard['b3'])} | {str(self.gameBoard['c3'])}\n\t -----------\n\t2 {str(self.gameBoard['a2'])} | {str(self.gameBoard['b2'])} | {str(self.gameBoard['c2'])}\n\t -----------\n\t1 {str(self.gameBoard['a1'])} | {str(self.gameBoard['b1'])} | {str(self.gameBoard['c1'])}\n\t  a   b   c" #Displays board with selections.
		
		#Comparison algorithm. It is reiterated for each possible winning combination and for both the player and artificial player. I will turn this into a module.
		if self.gameBoard["a3"] == self.playerSymbol and self.gameBoard["b3"] == self.playerSymbol and self.gameBoard["c3"] == self.playerSymbol: #Tries many combinations of winning moves.
			self.print_board() #Prints the most accurate board information.
			print(F"\n\n{self.playerName.title()} WINS!") #Prints a victory message.
			self.quit = True #Quit condition becomes true, signifying the game's end.

		elif self.gameBoard["a2"] == self.playerSymbol and self.gameBoard["b2"] == self.playerSymbol and self.gameBoard["c2"] == self.playerSymbol:
			self.print_board()
			print(F"\n{self.playerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["a1"] == self.playerSymbol and self.gameBoard["b1"] == self.playerSymbol and self.gameBoard["c1"] == self.playerSymbol:
			self.print_board()
			print(F"\n{self.playerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["a3"] == self.playerSymbol and self.gameBoard["a2"] == self.playerSymbol and self.gameBoard["a1"] == self.playerSymbol:
			self.print_board()
			print(F"\n{self.playerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["b3"] == self.playerSymbol and self.gameBoard["b2"] == self.playerSymbol and self.gameBoard["b1"] == self.playerSymbol:
			self.print_board()
			print(F"\n{self.playerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["c3"] == self.playerSymbol and self.gameBoard["c2"] == self.playerSymbol and self.gameBoard["c1"] == self.playerSymbol:
			self.print_board()
			print(F"\n{self.playerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["a3"] == self.playerSymbol and self.gameBoard["b2"] == self.playerSymbol and self.gameBoard["c1"] == self.playerSymbol:
			self.print_board()
			print(F"\n{self.playerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["c3"] == self.playerSymbol and self.gameBoard["b2"] == self.playerSymbol and self.gameBoard["a1"] == self.playerSymbol:
			self.print_board()
			print(F"\n{self.playerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["a3"] == self.artificialPlayerSymbol and self.gameBoard["b3"] == self.artificialPlayerSymbol and self.gameBoard["c3"] == self.artificialPlayerSymbol:
			self.print_board()
			print(F"\n{self.artificialPlayerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["a2"] == self.artificialPlayerSymbol and self.gameBoard["b2"] == self.artificialPlayerSymbol and self.gameBoard["c2"] == self.artificialPlayerSymbol:
			self.print_board()
			print(F"\n{self.artificialPlayerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["a1"] == self.artificialPlayerSymbol and self.gameBoard["b1"] == self.artificialPlayerSymbol and self.gameBoard["c1"] == self.artificialPlayerSymbol:
			self.print_board()
			print(F"\n{self.artificialPlayerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["a3"] == self.artificialPlayerSymbol and self.gameBoard["a2"] == self.artificialPlayerSymbol and self.gameBoard["a1"] == self.artificialPlayerSymbol:
			self.print_board()
			print(F"\n{self.artificialPlayerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["b3"] == self.artificialPlayerSymbol and self.gameBoard["b2"] == self.artificialPlayerSymbol and self.gameBoard["b1"] == self.artificialPlayerSymbol:
			self.print_board()
			print(F"\n{self.artificialPlayerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["c3"] == self.artificialPlayerSymbol and self.gameBoard["c2"] == self.artificialPlayerSymbol and self.gameBoard["c1"] == self.artificialPlayerSymbol:
			self.print_board()
			print(F"\n{self.artificialPlayerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["a3"] == self.artificialPlayerSymbol and self.gameBoard["b2"] == self.artificialPlayerSymbol and self.gameBoard["c1"] == self.artificialPlayerSymbol:
			self.print_board()
			print(F"\n{self.artificialPlayerName.title()} WINS!")
			self.quit = True

		elif self.gameBoard["c3"] == self.artificialPlayerSymbol and self.gameBoard["b2"] == self.artificialPlayerSymbol and self.gameBoard["a1"] == self.artificialPlayerSymbol:
			self.print_board()
			print(F"\n{self.artificialPlayerName.title()} WINS!")
			self.quit = True

		else:
			print(self.gameBoardDisplay)
			

	def introduction(self):
		"""A pretty useless method, but I'd rather it be this way for modularity & expandability (can be upgraded later on)."""
		print(F"Welcome, {self.playerName.title()}!\nThis is a simple game of Tic Tac Toe.")

	def tic_tac_toe(self):
		"""Manages the game's main operations. Calls methods & updates attributes in the necessary order, similarly to a regular main function."""

		#Introduce the game
		self.introduction()

		#Player selects their symbol.
		self.player_symbol_selection() 

		#Artificial player's symbol is selected based on player's selection. !I can randomize the selection. !I can add difficulty levels. !I can add a system of rounds & do best-out-of games. !I can  add the ability to play against other real users.
		self.artificial_player_symbol_selection() 

		#The game board is printed.
		self.print_board()

		#The first choice is made by either the player or the artificial player based on their symbols. The board is updated & printed again based on the choice made. The game then cont
		if self.playerSymbol == "X":
			self.determine_victor()
			self.player_choice()
			self.determine_victor()
		
		#The game instance.
		while True: 
			#The artificial player makes a choice.
			self.artificial_player_choice()

			#Check to see if anyone has won & print the board.
			self.determine_victor()

			#If someone did win, end the game.
			if self.quit == True:
				sys.exit()

			#The player makes a choice.
			self.player_choice()

			#Check to see if anyone wins & print the board.
			self.determine_victor()

			#If someone wins, end the game.
			if self.quit == True:
				sys.exit()
		
main()