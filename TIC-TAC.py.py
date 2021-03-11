board=['' for x in range (10)]


def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def insertLetter(letter,position):
    board[position]=letter

def spaceIsFree (position):
    return board[position]==' '

def printBoard(board):
    print('   |   |   ')
    print(''+board[1]+'|'+board[2]+' | '+board[3])
    print('   |   |   ')
    print('-------------------')
    print('   |   |   ')
    print('' + board[4] + '|' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-------------------')
    print('   |   |   ')
    print('' + board[7] + '|' + board[8] + ' | ' + board[9])
    print('   |   |   ')


def isWinner(board,letter):
    return ( board[7]==letter and board[8]==letter and board[9]==letter ) or ( board[1]==letter and board[2]==letter and board[3]==letter ) or ( board[4]==letter and board[5]==letter and board[6]==letter ) or ( board[1]==letter and board[4]==letter and board[7]==letter ) or ( board[2]==letter and board[8]==letter and board[5]==letter ) or ( board[3]==letter and board[6]==letter and board[9]==letter ) or ( board[1]==letter and board[5]==letter and board[9]==letter ) or ( board[3]==letter and board[5]==letter and board[7]==letter )

def playerMove():
    run = True

    while run :
        move = input('plaese select a position (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run =False
                    insertLetter('X',move)

                else:
                    print('Sorry the place is occupied, insert another position.')

            else:
                print('Please insert a valid number.')

        except:
            print('please type a number.')



def compMove():
    pass

def selectRandom(board):
    pass

def main():
    print ('Welcome to my silly game -_-')
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
              print(' O won this time')
              break

        if not (isWinner(board,'X')):
            compMove()
            printBoard(board)
        else:
              print('Congratulations! you won this game')
              break


    if (isBoardFull(board)):
         print('Tie match!')






