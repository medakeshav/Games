import textwrap
from random import randint



#Creating and printing the board
board = []
for x in range(5):
    board.append([0] * 5)
print "Minesweeper 5x5 !"
Rules  = raw_input("For Instructions input (Y/N):")

if Rules.lower() == "y":
    instruction_text = '''The objective is to guess the location of mines in a play field.Each square in the 5x5 play field is represented by 'O', behind which are mines hidden denoted by 'X'.You can start uncovering the 'O's by inputing the row and column number(0 to 4) you want to uncover.Each square will have the value = number of mines which are one square away from it.You need to uncover all the squares without hitting the uncovering the mines('X').In your first try you will have to take a Leap of faith not to step on a mine. Good luck !!'''
    dedented_text = textwrap.dedent(instruction_text).strip()
    print textwrap.fill(dedented_text, width=60)



disp_board = []

for x in range(5):
    disp_board.append(["O"] * 5)

def print_board(disp_board):
    for row in disp_board:
       print " ".join(row)

print_board(disp_board)


#Assigning random positions to Ships
mine_row = []
mine_col = []
def random_pos(board):
    for i in range(5):
        mine_row.append(randint(0, len(board) -1 ))
        mine_col.append(randint(0, len(board[0])-1 ))

random_pos(board)
#print mine_row
#print mine_col

def update_board(mine_row,mine_col):
    aroundx = [1,0,-1,0,1,1,-1,-1]
    aroundy = [0,1,0,-1,1,-1,1,-1]
    for i,j in zip(mine_row,mine_col):
        board[i][j] = "X"
        for a,b in zip(aroundx,aroundy):
            if  (i+a) >= 0 and (i+a) <5 and (j+b) >=0 and (j+b) <5:
                if board[i+a][j+b] <> "X":
                    board[i+a][j+b] +=  1     
    
    #print board

update_board(mine_row,mine_col)


def disp_board2(board):
    disp_board2=[]
    for x in range(5):
        disp_board2.append([0] * 5)
    
    for i in range(5):
        for j in range(5):
            disp_board2[i][j] = str(board[i][j])
    #1print_board(disp_board2)

disp_board2(board)

for i in range(10):

    guess_row = int(raw_input("Guess the row:"))
    guess_col = int(raw_input("Guess the col:"))


    if  board[guess_row][guess_col] == "X":
        disp_board[guess_row][guess_col] = str(board[guess_row][guess_col])
        print_board(disp_board)
        print "Boooom! You hit a mine"
        print "You lose, Try Again"
        break
    else:
        disp_board[guess_row][guess_col] = str(board[guess_row][guess_col])
        print_board(disp_board)
