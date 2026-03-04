print("Гра хрестики нолики :")
print("==================")

def create_board():                #     створили дошку
    return [" "] * 9

def show_board(b):
    print(b[0],  "|", b[1], "|", b[2])             #     показує дошку
    print("--|---|--")
    print(b[3],  "|", b[4], "|", b[5])
    print("--|---|--")
    print(b[6],  "|", b[7], "|", b[8])


def move(b, player):
    pos = int(input(f"Хід {player}. Введи число 1-9: ")) - 1
    if 0 <= pos <= 8 and b[pos] == " ":                            #  pos - це позиція клітинки , і перевіряє
        b[pos] = player                                      #    чи пуста клітинка
    else:
        print("Невірно! Спробуй ще раз.")
        move(b, player)


def winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),          #    список перевіряє рядки , колонки , діагональ чи збігаються
            (0,3,6),(1,4,7),(2,5,8),                 #     играшні позиції з Х і 0
            (0,4,8),(2,4,6)]
    for a,b1,c in wins:
        if b[a] == b[b1] == b[c] != " ":
            return True


def game():
    board = create_board()           #   головна гра де показує дошку , ходе Х, дошка має 9 кліток
    player = "X"                   #   перевіряє на перемогу або нечію
    for _ in range(9):
        show_board(board)
        move(board, player)
        if winner(board):
            show_board(board)
            print("Переміг", player)
            return
        player = "O" if player == "X" else "X"
    show_board(board)
    print("Нічия!")

game()

