from partsgame import Board, FieldIndexError, CellOccupiedError


def main():
    """Основная логика игры крестики-нолики."""
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:
        print(f'Ход делают {current_player}')

        # Запускается бесконечный цикл.
        while True:
            try:
                # Координаты ячейки, которые задает пользователь.
                row = int(input('Введите номер строки: ')) - 1
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: ')) - 1
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(f'Значение должно быть от 1 до {game.field_size}.')
                continue
            except ValueError:
                print(f'Допускаются только цифры от 1 до {game.field_size}.')
                print('Пожалуйста введите данные для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Введите другие координаты.')
            except Exception:
                print(f'Возникла ошибка: {Exception}')
            else:
                break

        # Здесь координаты передаются на поле.
        game.make_move(row, column, current_player)
        game.display()
        check_win(game)
        is_board_full(game)
        if check_win(game):
            if current_player == 'X':
                print('Выйграли крестики! Игра окончена.')
                break
            else:
                print('Выйграли нолики! Игра окончена.')
                break
        if is_board_full(game) == 0:
            print('Ничья! Игра окончена.')
            break
        current_player = 'O' if current_player == 'X' else 'X'


def is_board_full(game):
    """Цикл, который проверяет количество оставшихся свободных ячеек."""
    count = 0
    for line_field in game.board:
        for point in line_field:
            if point == ' ':
                count += 1
    if count == 0:
        return 0


def check_win(game):
    """Цикл, который проверяет комбинации для победы."""
    if (
            # Комбинации для строк
            game.board[0][0] == game.board[0][1] == game.board[0][2] == 'X'
            or game.board[0][0] == game.board[0][1] == game.board[0][2] == 'O'
            or game.board[1][0] == game.board[1][1] == game.board[1][2] == 'X'
            or game.board[1][0] == game.board[1][1] == game.board[1][2] == 'O'
            or game.board[2][0] == game.board[2][1] == game.board[2][2] == 'X'
            or game.board[2][0] == game.board[2][1] == game.board[2][2] == 'O'

            # Комбинации для столбцов
            or game.board[0][0] == game.board[1][0] == game.board[2][0] == 'X'
            or game.board[0][0] == game.board[1][0] == game.board[2][0] == 'O'
            or game.board[0][1] == game.board[1][1] == game.board[2][1] == 'X'
            or game.board[0][1] == game.board[1][1] == game.board[2][1] == 'O'
            or game.board[0][2] == game.board[1][2] == game.board[2][2] == 'X'
            or game.board[0][2] == game.board[1][2] == game.board[2][2] == 'O'

            # Комбинации для диагоналей
            or game.board[0][0] == game.board[1][1] == game.board[2][2] == 'X'
            or game.board[0][0] == game.board[1][1] == game.board[2][2] == 'O'
            or game.board[0][2] == game.board[1][1] == game.board[2][0] == 'X'
            or game.board[0][2] == game.board[1][1] == game.board[2][0] == 'O'
    ):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
