def make_matr():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        matrix.append(row)
    return matrix

def mprint(a):
    for row in a:
        print(' | '.join(row))

def win_comb(matrix):
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
           ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
           ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for comb in win:
        if matrix[comb[0][0]][comb[0][1]] == matrix[comb[1][0]][comb[1][1]] == matrix[comb[2][0]][comb[2][1]] != ' ':
            return matrix[comb[0][0]][comb[0][1]]
    return False

def take_input(player, matrix):
    flag = False
    while not flag:
        try:
            player_num = int(input(f'Enter the number you want to bet on {player} (1-9): '))
        except ValueError:
            print('Incorrect input. Please enter a number!')
            continue
        if 1 <= player_num <= 9:
            row = (player_num - 1) // 3
            col = (player_num - 1) % 3
            if matrix[row][col] == ' ':
                matrix[row][col] = player
                flag = True
            else:
                print('This cell is occupied. Please select another cell.')
        else:
            print('Incorrect input. Please enter a number in the range 1-9.')

matrix = make_matr()
count = 0
win = False
while not win:
    mprint(matrix)
    if count % 2 == 0:
        take_input('X', matrix)
    else:
        take_input('O', matrix)
    count += 1
    if count > 4:
        chek = win_comb(matrix)
        if chek:
            print(chek, 'wins!')
            win = True
            break
    if count == 9:
        print('Game draw!')
        break

mprint(matrix)