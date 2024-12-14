with open('input.txt') as f:
    data = f.read()

diskIdNumber = 0
blocksList = []
for i, value in enumerate(list(data)):
    if i % 2 == 0:
        for disk in range(0, int(value)):
            blocksList.append(diskIdNumber)
        diskIdNumber += 1
    else:
        for freeSpace in range(0, int(value)):
            blocksList.append('.')

freeSpacePositions = [i for i, value in enumerate(blocksList) if value == '.']
reversedBlocksList = blocksList[::-1]
filesWithoutFreeSpace = [None] * len(blocksList)
movedFiles = []

for index in range(len(reversedBlocksList)):
    if reversedBlocksList[index] == '.' or reversedBlocksList[index] in movedFiles:
        continue
    numberOfFiles = blocksList.count(reversedBlocksList[index])
    if len(freeSpacePositions) > 0:
        if(freeSpacePositions[0] < len(reversedBlocksList) - (index + 1)):
            replaceFile = True
            indexForReplace = []
            for position in freeSpacePositions:
                indexForReplace = []
                startedIndex = position
                for j in range(0, numberOfFiles):
                    if j == 0:
                        indexForReplace.append(position)
                    else:
                        if startedIndex + j not in freeSpacePositions:
                            break
                        indexForReplace.append(startedIndex + j)
                if len(indexForReplace) == numberOfFiles:
                    replaceFile = True
                    break
                else:
                    replaceFile = False
            if replaceFile:
                for j in indexForReplace:
                    filesWithoutFreeSpace[j] = reversedBlocksList[index]
                    freeSpacePositions.remove(j)
            else:
                for j in range(0, numberOfFiles):
                    filesWithoutFreeSpace[len(reversedBlocksList) - (index + (j + 1))] = reversedBlocksList[index]
        else:
            for j in range(0, numberOfFiles):
                filesWithoutFreeSpace[len(reversedBlocksList) - (index + (j + 1))] = reversedBlocksList[index]
        movedFiles.append(reversedBlocksList[index])

sum = 0

for i, value in enumerate(filesWithoutFreeSpace):
    if value is not None:
        sum += i * int(value)

print(sum)