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

for index in range(len(reversedBlocksList)):
    if reversedBlocksList[index] == '.':
        continue

    if len(freeSpacePositions) > 0:
        if(freeSpacePositions[0] < len(reversedBlocksList) - (index + 1)):
            filesWithoutFreeSpace[freeSpacePositions[0]] = reversedBlocksList[index]
            freeSpacePositions.pop(0)
        else:
            filesWithoutFreeSpace[len(reversedBlocksList) - (index + 1)] = reversedBlocksList[index]

sum = 0

for i, value in enumerate(filesWithoutFreeSpace):
    if value is not None:
        sum += i * int(value)

print(sum)