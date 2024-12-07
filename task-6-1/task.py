with open('input.txt') as f:
    data = f.read().split('\n')

maxNumberOfRows = len(data)
maxNumberOfColumns = len(data[0])
positionOfGuard = next(((row_index, row.index('^')) for row_index, row in enumerate(data) if '^' in row), None)
guardPositionRow = positionOfGuard[0]
guardPositionColumn = positionOfGuard[1]
isOutside = False
moveDirection = 'up'

while not isOutside:
    data[guardPositionRow] = data[guardPositionRow][:guardPositionColumn] + 'X' + data[guardPositionRow][guardPositionColumn + 1:]
    match moveDirection:
        case 'up':
            guardPositionRow -= 1
        case 'down':
            guardPositionRow += 1
        case 'left':
            guardPositionColumn -= 1
        case 'right':
            guardPositionColumn += 1
    if(guardPositionRow >= 0 and guardPositionRow < maxNumberOfRows and guardPositionColumn >= 0 and guardPositionColumn < maxNumberOfColumns and data[guardPositionRow][guardPositionColumn] == '#'):
        match moveDirection:
            case 'up':
                moveDirection = 'right'
                guardPositionRow += 1
                continue  
            case 'down':
                moveDirection = 'left'
                guardPositionRow -= 1
                continue  
            case 'left':
                moveDirection = 'up'
                guardPositionColumn += 1
                continue  
            case 'right':
                moveDirection = 'down'
                guardPositionColumn -= 1
                continue  
    if(guardPositionRow < 0 or guardPositionRow >= maxNumberOfRows or guardPositionColumn < 0 or guardPositionColumn >= maxNumberOfColumns):
        isOutside = True
        break


print(sum(row.count('X') for row in data))