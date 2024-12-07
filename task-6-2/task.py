with open('input.txt') as f:
    data = f.read().split('\n')

maxNumberOfRows = len(data)
maxNumberOfColumns = len(data[0])
positionOfGuard = next(((row_index, row.index('^')) for row_index, row in enumerate(data) if '^' in row), None)
startGuardPositionRow = positionOfGuard[0]
startGuardPositionColumn = positionOfGuard[1]
countInfiniteLoops = 0

for i in range(maxNumberOfRows):
    for j in range(maxNumberOfColumns):
        moveDirection = 'up'
        valueOnPosition = data[i][j]
        guardPositionRow = startGuardPositionRow
        guardPositionColumn = startGuardPositionColumn
        data[i] = data[i][:j] + 'O' + data[i][j + 1:]
        visited_states = set()
        while True:
            current_state = (guardPositionRow, guardPositionColumn, moveDirection)
            if current_state in visited_states:
                countInfiniteLoops += 1
                break
            visited_states.add(current_state)
            match moveDirection:
                case 'up':
                    guardPositionRow -= 1
                case 'down':
                    guardPositionRow += 1
                case 'left':
                    guardPositionColumn -= 1
                case 'right':
                    guardPositionColumn += 1
            if(guardPositionRow >= 0 and guardPositionRow < maxNumberOfRows and guardPositionColumn >= 0 and guardPositionColumn < maxNumberOfColumns and (data[guardPositionRow][guardPositionColumn] == '#' or data[guardPositionRow][guardPositionColumn] == 'O')):
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
                break
        data[i] = data[i][:j] + valueOnPosition + data[i][j + 1:]

print(countInfiniteLoops)