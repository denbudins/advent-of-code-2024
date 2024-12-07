inputFile = open("input.txt", "r")
content = inputFile.read()
inputFile.close()
splitContent = content.split("\n")
array1 = []
array2 = []
sum = 0
for locations in splitContent:
    location = locations.split()
    for i, loc in enumerate(location):
        if i % 2 == 0:
            array1.append(int(loc))
        else:
            array2.append(int(loc))
array1.sort()
array2.sort()
for i, value in enumerate(array1):
    sum += abs(value - array2[i])
print('total distance:', sum)
