playing_field = [" ", "0", "1", "2", "0", "&1", "&2", "&3", "1", "&5", "&6", "&7", "2", "&8", "&9", "&10"]
winning_combinations = [[5, 6, 7], [9, 10, 11], [13, 14, 15], [7, 10, 13], [5, 10, 15], [6, 10, 14], [5, 9, 13],
                        [7, 11, 15]]
step_index = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


def print_playing_field():
    print(playing_field[0], end=" ")
    print(playing_field[1], end=" ")
    print(playing_field[2], end=" ")
    print(playing_field[3])

    print(playing_field[4], end=" ")
    print(playing_field[5], end=" ")
    print(playing_field[6], end=" ")
    print(playing_field[7])

    print(playing_field[8], end=" ")
    print(playing_field[9], end=" ")
    print(playing_field[10], end=" ")
    print(playing_field[11])

    print(playing_field[12], end=" ")
    print(playing_field[13], end=" ")
    print(playing_field[14], end=" ")
    print(playing_field[15])


def step_playing_field(step, symbol):
    playing_field[step + 4] = symbol


def get_result():
    winner = ""
    for i in winning_combinations:
        if playing_field[i[0]] == "X" and playing_field[i[1]] == "X" and playing_field[i[2]] == "X":
            winner = "Пользователь 1"
        if playing_field[i[0]] == "O" and playing_field[i[1]] == "O" and playing_field[i[2]] == "O":
            winner = "Пользователь 2"
    return winner


game_over = False
player1 = True

while game_over == False:
    print_playing_field()

    if player1 == True:
        step = int(input("Человек 1, ваш ход. Ваш символ 'X'. Введите цифру после знака & на игровом поле"))
        symbol = "X"
    else:
        step = int(input("Человек 2, ваш ход. Ваш символ 'O'. Введите цифру после знака & на игровом поле"))
        symbol = "O"

    step_playing_field(step, symbol)
    winner = get_result()
    if winner != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

print_playing_field()
print("Победил", winner)