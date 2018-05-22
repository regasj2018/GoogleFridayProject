import random
#Board
board = []

for x in range(0,4):
  board.append(["O"] * 4)

def print_board(board):
  for row in board:
    print " ".join(row)

print "THIS. IS. BATTLESHIP! Enter in coordinates in a 4 by 4 grid. Remember 0 is still a position in python, so only use numbers 0-3."
print_board(board)
#Hidden Battleship
def random_row(board):
  return random.randint(0,len(board)-1)

def random_col(board):
  return random.randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)
#Guessing where the hidden ship is
for turn in range(4):
	guess_row = input("Guess Row:")
	guess_col = input("Guess Column:")
#Possible outcomes from guessing
	if guess_row == ship_row and guess_col == ship_col:
	  print "You sunk my battleship!"
	  break
	else:
		if turn == 3:
			board[guess_row][guess_col] = "X"
			print_board(board)
			print "Game Over"
			print "My ship was here: [" + str(ship_row) + "][" + str(ship_col) + "]"
		else:
			if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
				print "That's not even on the board."
			elif(board[guess_row][guess_col] == "X"):
				print "You guessed that one already."
			else:
				print "You missed my battleship!"
				board[guess_row][guess_col] = "X"
			print (turn + 1)
			print_board(board)
