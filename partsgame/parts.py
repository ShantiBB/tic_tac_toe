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

    def check_win(self, player):
        """Цикл, который проверяет комбинации для победы."""
        for i in range(self.field_size):
            if (
                    all([self.board[i][j] == player for j in range(self.field_size)])
                    or all([self.board[j][i] == player for j in range(self.field_size)])
            ):
                return True
        if (
                # Комбинации для диагоналей
                self.board[0][0] == self.board[1][1] == self.board[2][2] == player
                or self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True
        return False

    def is_board_full(self):
        """Цикл, который проверяет количество оставшихся свободных ячеек."""
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    def __str__(self):
        return f'Объект игрового поля размером {self.field_size}x{self.field_size}'
