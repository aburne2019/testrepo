from random import randint

board = [] # creates empty list for board

for x in range(5):
  board.append(["O"] * 5) # creates board of 5 by 5

def print_board(board):
  for row in board:
    print (" ".join(row)) # makes board only have O's

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board) # creates a random ship position
ship_col = random_col(board)
# print ship_row
# print ship_col

for turn in range(4): # limits user to 4 turns
  print ("Turn", turn + 1) # shows current turn

  guess_row = int(input("Guess Row: "))  # user inputs their guess for the row
  guess_col = int(input("Guess Col: "))  # user inputs their guess for the col

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sunk my battleship!")
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print ("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"       # prints an X in the spot of the miss on the board

      print_board(board)
    if turn == 3:
      print ("Game Over")