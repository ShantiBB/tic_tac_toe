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
        if game.check_win(current_player):
            if current_player == 'X':
                print('Выйграли крестики! Игра окончена.')
                break
            else:
                print('Выйграли нолики! Игра окончена.')
                break
        if game.is_board_full():
            print('Ничья! Игра окончена.')
            break
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
