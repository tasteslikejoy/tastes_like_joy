table = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]
def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][2] == player and board:
            return True

        if board[0][0] == player and board[1][1] == player and board[2][0] == player:
            return True

        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True

current_player = 'x'

while True:
    print_board(table)
    print('Ход игрока', current_player)
    row = int(input('Введите  номер строки:')) - 1
    col = int(input('Введите номер столбца:')) - 1

    if table[row][col] != '_':
        print('Ячейка занята')
        continue

    table[row][col] = current_player

    if check_win(table, current_player):
        print_board(table)
        print(f'Игрок {current_player} выиграл!!!')
        break

    if all([cell != '_' for row in table for cell in row]):
        print('Ничья!!!')
        print_board()
        break

    current_player = '0' if current_player == 'x' else 'x'