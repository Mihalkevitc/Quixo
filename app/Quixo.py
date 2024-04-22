import random

def create_board():
    """
    Создает пустую доску для игры в крестики-нолики.

    Returns:
    list: Двумерный список, представляющий игровую доску.
    """
    return [['-' for _ in range(5)] for _ in range(5)]

def display_board(board):
    """
    Отображает текущее состояние игровой доски.

    Args:
    board (list): Двумерный список, представляющий игровую доску.
    """
    for row in board:
        print(' '.join(row))
    print()

def check_win(board, symbol):
    """
    Проверяет, есть ли выигрышная комбинация на игровой доске.

    Args:
    board (list): Двумерный список, представляющий игровую доску.
    symbol (str): Символ игрока ('X' или 'O').

    Returns:
    bool: True, если найдена выигрышная комбинация, иначе False.
    """
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for col in range(5):
        if all(board[row][col] == symbol for row in range(5)):
            return True
    if all(board[i][i] == symbol for i in range(5)) or all(board[i][4-i] == symbol for i in range(5)):
        return True
    return False

def player_move(board, symbol):
    """
    Выполняет ход игрока.

    Args:
    board (list): Двумерный список, представляющий игровую доску.
    symbol (str): Символ игрока ('X' или 'O').

    Returns:
    list: Обновленное состояние игровой доски.
    """
    while True:
        row, col = map(int, input(f'Введите координаты для символа "{symbol}" (строка столбец): ').split())
        if 0 <= row < 5 and 0 <= col < 5 and board[row][col] == '-':
            board[row][col] = symbol
            break
        else:
            print('Некорректный ход. Попробуйте еще раз.')
    return board

def computer_move(board, symbol):
    """
    Выполняет ход компьютера.

    Args:
    board (list): Двумерный список, представляющий игровую доску.
    symbol (str): Символ компьютера ('X' или 'O').

    Returns:
    list: Обновленное состояние игровой доски.
    """
    available_moves = [(row, col) for row in range(5) for col in range(5) if board[row][col] == '-']
    row, col = random.choice(available_moves)
    board[row][col] = symbol
    return board

def play_game():
    """
    Основной игровой цикл.
    """
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
