#Sam Gordon Tic Tac Toe


def draw_board(spots):
    board = (f'|{spots[1]}|{spots[2]}|{spots[3]}|\n'
                f'|{spots[4]}|{spots[5]}|{spots[6]}|\n'
                f'|{spots[7]}|{spots[8]}|{spots[9]}|')
    print(board)

def check_turn(turn):
    if turn % 2 == 0: return 'O'
    else: 
        return 'x'

def check_win(spots):
    if (spots[1] == spots[2] == spots[3])\
        or (spots[4] == spots[5] == spots[6])\
        or (spots[7] == spots[8] == spots[9]):
        return True
    elif (spots[1] == spots[4] == spots[7])\
        or (spots[2] == spots[5] == spots[8])\
        or (spots[3] == spots[6] == spots[9]):
        return True
    elif (spots[1] == spots[5] == spots[9])\
        or(spots[3] == spots[5] == spots[7]):
        return True 
    else: 
        return False

spots = {1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',}

playing = True
win = False 
turn = 0

print('Enter q to quit game')

while playing: 
    draw_board(spots)
    print(f"Player {str((turn % 2) +1 )}'s turn")
    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {'X', 'O'}:
            turn += 1
            spots[int(choice)] = check_turn(turn)

    if check_win(spots): 
        playing = False
        win = True
    if turn > 8:
        playing = False
draw_board(spots)
if win: 
    if check_turn(turn) == 'X':
        print('player 1 wins')
    else:
        print('Player 2 wins')
else:
    print('no one wins')

print('Thanks for playing')