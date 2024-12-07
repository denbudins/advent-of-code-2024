with open('input.txt') as f:
    data = f.read().split('\n')

arrayLength = len(data)
columnLength = len(data[0])
sumOfXmas = 0

for row in range(arrayLength):
    for column in range(columnLength):
        if column + 3 < columnLength and data[row][column] == 'X' and data[row][column + 1] == 'M' and data[row][column + 2] == 'A' and data[row][column + 3] == 'S':
            sumOfXmas += 1
        if row + 3 < arrayLength and data[row][column] == 'X' and data[row + 1][column] == 'M' and data[row + 2][column] == 'A' and data[row + 3][column] == 'S':
            sumOfXmas += 1
        if row + 3 < arrayLength and column + 3 < columnLength and  data[row][column] == 'X' and data[row + 1][column + 1] == 'M' and data[row + 2][column + 2] == 'A' and data[row + 3][column + 3] == 'S':
            sumOfXmas += 1
        if row + 3 < arrayLength and column + 3 < columnLength and data[row + 3][column] == 'X' and data[row + 2][column + 1] == 'M' and data[row + 1][column + 2] == 'A' and data[row][column + 3] == 'S':
            sumOfXmas += 1
        if column + 3 < columnLength and data[row][column + 3] == 'X' and data[row][column + 2] == 'M' and data[row][column + 1] == 'A' and data[row][column] == 'S':
            sumOfXmas += 1
        if row + 3 < arrayLength and data[row + 3][column] == 'X' and data[row + 2][column] == 'M' and data[row + 1][column] == 'A' and data[row][column] == 'S':
            sumOfXmas += 1
        if row + 3 < arrayLength and column + 3 < columnLength and  data[row + 3][column + 3] == 'X' and data[row + 2][column + 2] == 'M' and data[row + 1][column + 1] == 'A' and data[row][column] == 'S':
            sumOfXmas += 1
        if row + 3 < arrayLength and column + 3 < columnLength and data[row][column + 3] == 'X' and data[row + 1][column + 2] == 'M' and data[row + 2][column + 1] == 'A' and data[row + 3][column] == 'S':
            sumOfXmas += 1
print(sumOfXmas)