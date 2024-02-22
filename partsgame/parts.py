class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(self.field_size)] for _ in range(self.field_size)]

    def make_move(self, row, column, player):
        self.board[row][column] = player

    # Метод, который отрисовывает игровое поле
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self):
        return f'Объект игрового поля размером {self.field_size}x{self.field_size}'
