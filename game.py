LEFT = 0
RIGHT = 1

column = 1

flipperList = [RIGHT, LEFT, RIGHT]

flipperListSecondLine = [RIGHT, LEFT, RIGHT]

flipperListThirdLine = [RIGHT, LEFT, RIGHT]

while column == 1 or column == 2 or column == 3 or column == 4:
    column = int(input('choose a number for start 1, 2, 3, 4 \n'))
    if column == 1:
        if flipperList[0] == RIGHT:
            column = 2
            flipperList[0] = LEFT
        elif flipperList[0] == LEFT:
            column = 1
            flipperList[0] = RIGHT

    elif column == 2:
        if flipperList[0] == RIGHT:
            column = 2
            flipperList[0] = LEFT
        elif flipperList[0] == LEFT:
            column = 1
            flipperList[0] = RIGHT
        elif flipperList[1] == RIGHT:
            column = 3
            flipperList[1] = LEFT
        elif flipperList[1] == LEFT:
            column = 2
            flipperList[1] = RIGHT

    elif column == 3:
        if flipperList[1] == RIGHT:
            column = 3
            flipperList[1] = LEFT
        elif flipperList[1] == LEFT:
            column = 2
            flipperList[1] = RIGHT
        elif flipperList[2] == RIGHT:
            column = 4
            flipperList[2] = LEFT
        elif flipperList[2] == LEFT:
            column = 3
            flipperList[2] = RIGHT

    elif column == 4:
        if flipperList[2] == RIGHT:
            column = 4
            flipperList[2] = LEFT
        elif flipperList[2] == LEFT:
            column = 3
            flipperList[2] = RIGHT
    if column == 1 or column == 2 or column == 3 or column == 4:
        print(f'from column: {column} ')

    if column == 1:
        if flipperListSecondLine[0] == RIGHT:
            column = 2
            flipperListSecondLine[0] = LEFT
        elif flipperListSecondLine[0] == LEFT:
            column = 1
            flipperListSecondLine[0] = RIGHT

    elif column == 2:
        if flipperListSecondLine[0] == RIGHT:
            column = 2
            flipperListSecondLine[0] = LEFT
        elif flipperListSecondLine[0] == LEFT:
            column = 1
            flipperListSecondLine[0] = RIGHT
        elif flipperListSecondLine[1] == RIGHT:
            column = 3
            flipperListSecondLine[1] = LEFT
        elif flipperListSecondLine[1] == LEFT:
            column = 2
            flipperListSecondLine[1] = RIGHT

    elif column == 3:
        if flipperListSecondLine[1] == RIGHT:
            column = 1
            flipperListThirdLine[0] = RIGHT

    elif column == 2:
        if flipperListThirdLine[0] == RIGHT:
            column = 2
            flipperListThirdLine[0] = LEFT
        elif flipperListThirdLine[0] == LEFT:
            column = 1
            flipperListThirdLine[0] = RIGHT
        elif flipperListThirdLine[1] == RIGHT:
            column = 3
            flipperListThirdLine[1] = LEFT
        elif flipperListThirdLine[1] == LEFT:
            column = 2
            flipperListThirdLine[1] = RIGHT

    elif column == 3:
        if flipperListThirdLine[1] == RIGHT:
            column = 3
            flipperListThirdLine[1] = LEFT
        elif flipperListThirdLine[1] == LEFT:
            column = 2
            flipperListThirdLine[1] = RIGHT
        elif flipperListThirdLine[2] == RIGHT:
            column = 4
            flipperListThirdLine[2] = LEFT
        elif flipperListThirdLine[2] == LEFT:
            column = 3
            flipperListThirdLine[2] = RIGHT

    elif column == 4:
        if flipperListThirdLine[2] == RIGHT:
            column = 4
            flipperListThirdLine[2] = LEFT
        elif flipperListThirdLine[2] == LEFT:
            column = 3
            flipperListThirdLine[2] = RIGHT
    if column == 1 or column == 2 or column == 3 or column == 4:
        print(f'ending column: {column}')
