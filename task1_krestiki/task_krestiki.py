# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP


matric = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print(f'{matric[0]}\n{matric[1]}\n{matric[2]}')
print(matric[0][0])
x, y = 0, 0
count = 0
countX = 0
count0 = 0
play = True
while play:

    while count < 4:
        print('Чтобы поставить крестик введите координаты клетки: х и у от 0 до 2')
        x, y = int(input('x - ')), int(input('y - '))
        while x not in [0, 1, 2] or y not in [0, 1, 2] or matric[x][y] != '*':
            print('Эта клетка занята или неверные координаты, чтобы поставить крестик введите другие координаты клетки: х и у от 0 до 2')
            x, y = int(input('x - ')), int(input('y - '))
        matric[x][y] = 'x'
        print(f'{matric[0]}\n{matric[1]}\n{matric[2]}')
        count +=1
        print('Чтобы поставить нолик введите координаты клетки: х и у от 0 до 2')
        x, y = int(input('x - ')), int(input('y - '))
        while matric[x][y] != '*' or x not in [0, 1, 2] or y not in [0, 1, 2]:
            print('Эта клетка занята или неверные координаты, чтобы поставить нолик введите другие координаты клетки: х и у от 0 до 2')
            x, y = int(input('x - ')), int(input('y - '))
        matric[x][y] = '0'
        print(f'{matric[0]}\n{matric[1]}\n{matric[2]}')
        count += 1
        print(count)

    print('Чтобы поставить крестик введите координаты клетки: х и у от 0 до 2')
    x, y = int(input('x - ')), int(input('y - '))
    while x not in [0, 1, 2] or y not in [0, 1, 2] or matric[x][y] != '*':
        print('Эта клетка занята или неверные координаты, чтобы поставить крестик введите другие координаты клетки: х и у от 0 до 2')
        x, y = int(input('x - ')), int(input('y - '))
    matric[x][y] = 'x'
    print(f'{matric[0]}\n{matric[1]}\n{matric[2]}')
    count += 1

    if count > 4 and count % 2 > 0:
        for x in range(0, 3):
            for y in range(0, 3):
                if matric[x][y] == 'x':
                    countX += 1
            if countX == 3:
                print('Победу одержал первый игрок')
                play = False
                break
            countX = 0
        for y in range(0, 3):
            for x in range(0, 3):
                if matric[x][y] == 'x':
                    countX += 1
            if countX == 3:
                print('Победу одержал первый игрок')
                play = False
                break
            countX = 0
        if matric[0][0] == 'x' and matric[1][1] == 'x' and matric[2][2] == 'x':
            print('Победу одержал первый игрок')
            play = False
            break
        if matric[0][2] == 'x' and matric[1][1] == 'x' and matric[2][0] == 'x':
            print('Победу одержал первый игрок')
            play = False
            break

    print('Чтобы поставить нолик введите координаты клетки: х и у от 0 до 2')
    x, y = int(input('x - ')), int(input('y - '))
    while x not in [0, 1, 2] or y not in [0, 1, 2] or matric[x][y] != '*':
        print(
            'Эта клетка занята или неверные координаты, чтобы поставить нолик введите другие координаты клетки: х и у от 0 до 2')
        x, y = int(input('x - ')), int(input('y - '))
    matric[x][y] = '0'
    print(f'{matric[0]}\n{matric[1]}\n{matric[2]}')
    count += 1

    if count > 4 and count % 2 == 0:
        for x in range(0, 3):
            for y in range(0, 3):
                if matric[x][y] == '0':
                    countX += 1
            if countX == 3:
                print('Победу одержал второй игрок')
                play = False
                break
            countX = 0
        for y in range(0, 3):
            for x in range(0, 3):
                if matric[x][y] == '0':
                    countX += 1
            if countX == 3:
                print('Победу одержал второй игрок')
                play = False
                break
            countX = 0
        if matric[0][0] == '0' and matric[1][1] == '0' and matric[2][2] == '0':
            print('Победу одержал второй игрок')
            play = False
            break
        if matric[0][2] == '0' and matric[1][1] == '0' and matric[2][0] == '0':
            print('Победу одержал второй игрок')
            play = False
            break
