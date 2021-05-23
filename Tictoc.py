
def print_playfield(playfiled):
    print("---------")
    print(f'| {playfiled[0][0]} {playfiled[0][1]} {playfiled[0][2]} |')
    print(f'| {playfiled[1][0]} {playfiled[1][1]} {playfiled[1][2]} |')
    print(f'| {playfiled[2][0]} {playfiled[2][1]} {playfiled[2][2]} |')
    print("---------")

def entering_position(user_move_, player, move, playfiled):
    while True:
        if not user_move_[0].isnumeric() or not user_move_[1].isnumeric():
            print("You should enter numbers!")
            return move

        user_move = [int(i) for i in user_move_]

        for i,j in enumerate(all_cor):
            for k,l in enumerate(j):
                if l == user_move:
                    position_move = [i, k]

        if user_move[0] > 3 or user_move[1] > 3:
            print("Coordinates should be from 1 to 3!")
            return move

        if all_[position_move[0]][position_move[1]] == 'X' or all_[position_move[0]][position_move[1]] == 'O':
            print("This cell is occupied! Choose another one!")
            return move
        else:
            all_[position_move[0]][position_move[1]] = player
            move += 1
            print_playfield(playfiled)
            return move

#podana in transponirana matrika
all_ = [['_','_','_'],['_','_','_'],['_','_','_']]
all_TR = [list(i) for i in zip(*all_)]

all_cor = [[[1, 3], [2, 3], [3, 3]], [[1, 2], [2, 2], [3, 2]], [[1, 1], [2, 1], [3, 1]]]



zeros_v= ['O' , 'O', 'O']
iks_v = ['X', 'X', 'X']
zeros_k= [['O'] , ['O'], ['O']]
iks_k = [['X'], ['X'], ['X']]

print_playfield(all_)
game_stage = 1
while True:
        #input igralca z koordinatami
        user_move_ = (input("Enter the cordinates:")).split()
        if game_stage % 2 == 0:
            player = 'O'
        else:
            player = 'X'

        game_stage = entering_position(user_move_, player, game_stage, all_)
        
        #pregled in print ce vsebuje ničle (vrstica, kolona)
        check_z_v = [x for x in all_ if ['O' , 'O', 'O'] in all_]
        check_z_k = [y for y in all_TR if ['O' , 'O', 'O'] in all_TR]

        #pregled in print ce vsebuje X (vrstica, kolona)
        check_x_v = [x for x in all_ if ['X', 'X', 'X'] in all_]
        check_x_k = [y for y in all_TR if ['X', 'X', 'X'] in all_TR]

        count = 0
        #stetje O in X
        sum_O = len([count + 1 for vrsta in all_ for x in vrsta if x == 'O'])
        sum_X = len([count + 1 for vrsta in all_ for y in vrsta if y == 'X'])

        #diagonali
        diagon_D = [all_[0][0], all_[1][1], all_[2][2]]
        diagon_L = [all_[2][0], all_[1][1], all_[0][2]]

        
        if (check_x_k != [] or check_x_v != [] or diagon_D == iks_v or diagon_L == iks_v) and not((abs(sum_O - sum_X)) >= 2):
            print("X wins")
            break
        elif (check_z_k != [] or check_z_v != [] or diagon_D == zeros_v or diagon_L == zeros_v) and not((abs(sum_O - sum_X)) >= 2):
            print("O wins")
            break
        if game_stage > 9 and ('_' not in all_):
            print('Draw')
            break

        


                






