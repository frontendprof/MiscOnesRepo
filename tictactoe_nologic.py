#BRR
#MSAW


theBoard = {'1': '-','2': '-','3': '-',
            '4': '-','5': '-','6': '-',
            '7': '-','8': '-','9': '-'}

def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])

    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])

    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

turn = 'X'
print(''' Pattern of: \n1 , 2 , 3 ,\n4 , 5 , 6 , \n7 , 8 , 9\n\n\n''')
for i in range(9):
    printBoard(theBoard)
    print('                 Turn for ' + turn)

    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
