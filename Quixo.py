import random

# Функция для создания пустой доски
def create_board():
    return [['-' for _ in range(5)] for _ in range(5)]

# Функция для отображения доски
def display_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Функция для проверки выигрышной комбинации
def check_win(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for col in range(5):
        if all(board[row][col] == symbol for row in range(5)):
            return True
    if all(board[i][i] == symbol for i in range(5)) or all(board[i][4-i] == symbol for i in range(5)):
        return True
    return False

# Функция для хода игрока
def player_move(board, symbol):
    while True:
        row, col = map(int, input(f'Введите координаты для символа "{symbol}" (строка столбец): ').split())
        if 0 <= row < 5 and 0 <= col < 5 and board[row][col] == '-':
            board[row][col] = symbol
            break
        else:
            print('Некорректный ход. Попробуйте еще раз.')
    return board

# Функция для хода компьютера
def computer_move(board, symbol):
    available_moves = [(row, col) for row in range(5) for col in range(5) if board[row][col] == '-']
    row, col = random.choice(available_moves)
    board[row][col] = symbol
    return board

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
