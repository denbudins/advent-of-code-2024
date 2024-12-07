inputFile = open("input.txt", "r")
content = inputFile.read()
inputFile.close()
splitContent = content.split("\n")
sum = 0
for i in splitContent:
    array = i.split(" ")
    isSafe = False
    differenceBetweenLevels = []
    for index, value in enumerate(array):
        if index < len(array) - 1:
            adjacentLevelDiffer = int(array[index + 1]) - int(value)
            differenceBetweenLevels.append(adjacentLevelDiffer)
            if abs(adjacentLevelDiffer) >= 1 and abs(adjacentLevelDiffer) <= 3:
                isSafe = True
            else:
                isSafe = False
                break
    if isSafe and (all(difference > 0 for difference in differenceBetweenLevels) or all(difference < 0 for difference in differenceBetweenLevels)):
        sum += 1
print(sum)