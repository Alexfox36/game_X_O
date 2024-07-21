

def greet():
    print(" -----------------")
    print("  Приветсвуем вас ")
    print("      в игре      ")
    print("  крестики- нолики")
    print(" -----------------")
    print(" формат ввода: х у")
    print(" х -  номер строки")
    print(" у - номер столбца")
    print(" -----------------")
    print("   Хорошей игры   ")
    print(" -----------------")
def show():
    print(f'   0  1  2')
    for el, row in enumerate(field):
        row_info = str(el) + " " + "  ".join(row) + "  "
        print(row_info)

def asking():
        while True:
            coord = input(" Ваш ход :").split()

            if len(coord) != 2:
                print("Введите 2 коордитаны")
                continue

            x, y = coord

            if not(x.isdigit()) or not(y.isdigit()):
                print("Введите числа")
                continue

            x, y = int(x), int(y)

            if  0 > x or x > 2 or 0 > y or y > 2:
                    print(" Координата вне диапазона ")
                    continue

            if field[x][y] != " ":
                    print("Ячейка занята!")
                    continue
            return x, y

def chek_win():
    win_poz = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
               ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
               ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for poz in win_poz:
        symbol = []

        for p in poz:
            symbol.append(field[p[0]][p[1]])

        if symbol == ["X", "X", "X"]:
            print("Победил крестик")
            return True
        if symbol == ["0", "0", "0"]:
            print("Победил нолик")
            return True
    return False

field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

greet()
show()

num = 0
while True:
    show()
    num += 1
    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = asking()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if chek_win():
        break

    if num == 9:
        print("Ничья!")
        break




