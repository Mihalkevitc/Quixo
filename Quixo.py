import random

# Функция для создания пустой доски
def create_board():
    return [['-' for _ in range(5)] for _ in range(5)]

# Функция для отображения доски
def display_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Основной игровой цикл
def play_game():
    board = create_board()
    symbols = ['X', 'O']
    random.shuffle(symbols)
    current_symbol = symbols[0]
    
    while True:
        display_board(board)
        
        if current_symbol == 'X':
            board = player_move(board, current_symbol)
        else:
            board = computer_move(board, current_symbol)
        
        if check_win(board, current_symbol):
            display_board(board)
            print(f'Игрок "{current_symbol}" выиграл!')
            break
        
        if all(all(cell != '-' for cell in row) for row in board):
            display_board(board)
            print('Ничья!')
            break
        
        current_symbol = symbols[1] if current_symbol == symbols[0] else symbols[0]

# Запуск игры
play_game()
