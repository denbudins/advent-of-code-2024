import itertools

def calculate_distance(antenna1, antenna2):
    return (antenna1[0] - antenna2[0], antenna1[1] - antenna2[1])

with open('input.txt') as f:
    data = f.read().split('\n')

antennas = {}
antinode = {}

for row in range(len(data)):
    for col in range(len(data[0])):
        char = data[row][col]
        if char == '.':
            continue
        if char not in antennas:
            antennas[char] = []
        antennas[char].append((row, col))

for key in antennas:
    pairs = itertools.combinations(antennas[key], 2)
    for pair in pairs:
        distance = calculate_distance(pair[0], pair[1])
        antinode1 = (pair[0][0] - distance[0], pair[0][1] - distance[1])
        while 0 <= antinode1[0] < len(data) and 0 <= antinode1[1] < len(data[0]):
            antinode[antinode1] = antinode1
            antinode1 = (antinode1[0] - distance[0], antinode1[1] - distance[1])
        
        antinode2 = (pair[1][0] + distance[0], pair[1][1] + distance[1])
        while 0 <= antinode2[0] < len(data) and 0 <= antinode2[1] < len(data[0]):
            antinode[antinode2] = antinode2
            antinode2 = (antinode2[0] + distance[0], antinode2[1] + distance[1])
        

print(len(antinode))