game_still_going=True

winner=None

current_player="X"


board = ['-','-','-',
         '-','-','-',
         '-','-','-']

def display_board():
    print(board[0]+ "|"+board[1]+"|"+ board[2])
    print(board[3]+ "|"+board[4]+"|"+ board[5])
    print(board[6]+ "|"+board[7]+"|"+ board[8])

#PLAY TIC-TAC-TOE
def play_game():

    #Display the board initially
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()


    #when game is done
    if winner=="X" or winner=="O":
        print(winner+" won")
    elif winner==None:
        print('Tie')

def handle_turn(player):


  print(player+"'s turn")
  pos=input("choose a number 1- 9:\n")
  while pos not in '1 2 3 4 5 6 7 8 9'.split():
    pos=input("!!!Invalid Input!!!....give me correct input you fool:\n")

  pos=int(pos)-1
  if board[pos]=='-':
    print("That's right baby\n")
    board[pos]=player
    #flip to other player
    flip_player()
    display_board()
  else:
    print("ERROR!! Position already used ","HEy",player,"..type again to see the board...you FOOL!!\n")




def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    global winner
    row_winner=check_rows()
    column_winner=check_columns()
    diagonal_winner=check_diagonals()

    if row_winner:
        winner=row_winner
        #a win
    elif column_winner:
        winner=column_winner
        # a win
    elif diagonal_winner:
        winner=diagonal_winner
        #a win
    else:
        pass#no win
    return True
def check_rows():
    global game_still_going

    row=[True,True,True]
    for i in range(3):
        row[i]=board[i]==board[i+1]==board[i+2] !="-"

    if True in row:
        game_still_going=False
    if row[0]:
        return board[0]
    elif row[1]:
        return board[3]
    elif row[2]:
        return board[6]

    return

def check_columns():
    global game_still_going

    column=[True,True,True]
    for i in range(3):
        column[i]=board[i]==board[i+3]==board[i+6] !="-"

    if True in column:
        game_still_going=False
    if column[0]:
        return board[0]
    elif column[1]:
        return board[1]
    elif column[2]:
        return board[2]

    return
    return

def check_diagonals():
    global game_still_going

    diagonals=[True,True]
    diagonals[0]=board[0]==board[4]==board[8] !='-'
    diagonals[1]=board[2]==board[4]==board[6] !='-'
    if True in diagonals:
        game_still_going=False
    if diagonals[0]:
        return board[0]
    elif diagonals[1]:
        return board[2]

    return
    return

def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going=False



    return


def flip_player():
  global current_player
  if current_player=="X":
    current_player="O"
  elif current_player=="O":
    current_player="X"
    return







play_game()



#board
#display
#play game
#check win
#check rows
#check compile
#check diagonal
#check Tie
#flip player
