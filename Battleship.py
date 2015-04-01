from random import randint
import sys
#Creating and printing the board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Welcome to the Single player version of a simplified Battleship Game!"
print "In a 5x5 playfield you need to guess the location of the ship"
print "Let's play Battleship!"
print_board(board)


#Assigning random positions to Ships
ship_row = []
ship_col = []
def random_pos(board):
    for i in range(5):
        ship_row.append(randint(0, len(board) - 1))
        ship_col.append(randint(0, len(board[0]) - 1))


random_pos(board)

#print ship_row
#print ship_col

print "Enter a number between 0 and 4"

# Everything from here on should go in your for loop!

for turn in range(0,10):
    print "Turn" , turn +1
    guess_row = raw_input("Guess Row:")
    guess_col = raw_input("Guess Col:")
    if (guess_row == "" or guess_col == "" or guess_col.isalpha() == True or guess_row.isalpha() == True or guess_col.isalnum() == True or guess_row.isalnum() == True):
        print "Please enter an integer"

    else:
        guess_row =int(guess_row)
        guess_col =int(guess_col)
        for i in range(5):
            if guess_row == ship_row[i] and guess_col == ship_col[i]:
                print "Congratulations! You sunk my battleship!"
                board[guess_row][guess_col] = "Y"
                break


        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print "Oops, that's not even on the board."
            if turn == 9:
                print "Game Over"
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            if turn == 9:
                print "Game Over"
        elif(board[guess_row][guess_col] <> "Y"):
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            if turn == 9:
                print "Game Over"
        else:
            a = 1
            # Print (turn + 1) here!
            print_board(board)

