lines = [
    [0,1,2],[3,4,5],[6,7,8],    #    рядки
    [0,3,6],[1,4,7],[2,5,8],    #    стовбчики
    [0,4,8],[2,4,6]             #    діагональ
]


def show(board):
    cells = [board[i] if board[i] != ' ' else str(i+1) for i in range(9)]
    print(f"\n {cells[0]} | {cells[1]} | {cells[2]}")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]}")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]}\n")

def winner(board):
    for a,b,c in lines:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

def main():
    board = [' ']*9
    player = 'X'

    while True:
        show(board)
        move = input(f"Хід {player}. Обери клітинку (1-9): ").strip()
        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Введи число від 1 до 9.")
            continue
        i = int(move) - 1
        if board[i] != ' ':
            print("Вже зайнято. Спробуй іншу клітинку.")
            continue

        board[i] = player
        w = winner(board)
        if w:
            show(board)
            print(f"Переміг {w}! ")
            break

        if ' ' not in board:
            show(board)
            print("Нічия ")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":

     main()
