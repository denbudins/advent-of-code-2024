with open('input.txt') as f:
    data = f.read().split('\n')

arrayLength = len(data)
columnLength = len(data[0])
sumOfXmas = 0

for row in range(arrayLength):
    for column in range(columnLength):
        if column + 2 < columnLength and row + 2 < arrayLength and data[row][column] == 'M' and data[row][column + 2] == 'M' and data[row + 2][column] == 'S'  and data[row + 2][column + 2] == 'S' and data[row + 1][column + 1] == 'A':
            sumOfXmas += 1
        if column + 2 < columnLength and row + 2 < arrayLength and data[row][column + 2] == 'M' and data[row + 2][column + 2] == 'M' and data[row][column] == 'S' and data[row + 2][column] == 'S' and data[row + 1][column + 1] == 'A':
            sumOfXmas += 1
        if column + 2 < columnLength and row + 2 < arrayLength and data[row][column] == 'M' and data[row + 2][column] == 'M' and data[row + 2][column + 2] == 'S' and data[row][column + 2] == 'S' and data[row + 1][column + 1] == 'A':
            sumOfXmas += 1
        if column + 2 < columnLength and row + 2 < arrayLength and data[row + 2][column] == 'M' and data[row + 2][column + 2] == 'M' and data[row][column] == 'S' and data[row][column + 2] == 'S' and data[row + 1][column + 1] == 'A':
            sumOfXmas += 1
print(sumOfXmas)