import pandas as pd

LEFT = 0
RIGHT = 1

column = 1

flipperList = [RIGHT, LEFT, RIGHT]

flipperListSecondLine = [RIGHT, LEFT, RIGHT]

flipperListThirdLine = [RIGHT, LEFT, RIGHT]

def isAvalidColumn(column):
    if column == 1 or column == 2 or column == 3 or column == 4:
        return True
    else:
        return False


data = [[RIGHT, LEFT, RIGHT],
        [RIGHT, LEFT, RIGHT],
        [RIGHT, LEFT, RIGHT]]


df = pd.DataFrame(data, columns=['Flipper Column 1', 'Flipper Column 2', 'Flipper Column 3'])
print(df)
while isAvalidColumn(column):
    column = int(input('choose a number for start 1, 2, 3, 4 \n'))
    if isAvalidColumn(column):
        print(f'from user: {column}')

    for line in range(3):
        if column == 1:
            if df.iloc[line, 0] == RIGHT:
                column = 2
                df.iloc[line, 0] = LEFT
            elif df.iloc[line, 0] == LEFT:
                column = 1
                df.iloc[line, 0] = RIGHT
            if isAvalidColumn(column) and not line == 2:
                print(f'from column: {column}')

        elif column == 2:
            if df.iloc[line, 0] == RIGHT:
                column = 2
                df.iloc[line, 0] = LEFT
            elif df.iloc[line, 0] == LEFT:
                column = 1
                df.iloc[line, 0] = RIGHT
            elif df.iloc[line, 1] == RIGHT:
                column = 3
                df.iloc[line, 1] = LEFT
            elif df.iloc[line, 1] == LEFT:
                column = 2
                df.iloc[line, 1] = RIGHT
            if isAvalidColumn(column) and not line == 2:
                print(f'from column: {column}')

        elif column == 3:
            if df.iloc[line, 1] == RIGHT:
                column = 3
                df.iloc[line, 1] = LEFT
            elif df.iloc[line, 1] == LEFT:
                column = 2
                df.iloc[line, 1] = RIGHT
            elif df.iloc[line, 2] == RIGHT:
                column = 4
                df.iloc[line, 2] = LEFT
            elif df.iloc[line, 2] == LEFT:
                column = 3
                df.iloc[line, 2] = RIGHT
            if isAvalidColumn(column) and not line == 2:
                print(f'from column: {column}')

        elif column == 4:
            if df.iloc[line, 2] == RIGHT:
                column = 4
                df.iloc[line, 2] = LEFT
            elif df.iloc[line, 2] == LEFT:
                column = 3
                df.iloc[line, 2] = RIGHT
            if isAvalidColumn(column) and not line == 2:
                print(f'from column: {column}')

    if isAvalidColumn(column):
        print(f'ending column: {column}')


