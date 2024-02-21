class Board:
    # Пустое поле 3х3
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    # Метод, который обрабатывает ход игрока
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, который отрисовывает игровое поле
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
