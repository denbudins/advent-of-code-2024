from collections import defaultdict

with open('input.txt') as f:
    data = f.read().split()

stones = defaultdict(int)
for stone in data:
    stone = int(stone)
    stones[stone] += 1

numberOfBlinking = 75
for i in range(numberOfBlinking):
    stonework = dict(stones)
    for stone, count in stonework.items():
        if count == 0: continue
        if stone == 0:
            stones[1] += count
            stones[0] -= count
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_len = int(len(stone_str) / 2)
            stone_1 = int(stone_str[:new_len])
            stone_2 = int(stone_str[new_len:])
            stones[stone_1] += count
            stones[stone_2] += count
            stones[stone] -= count
        else:
            stones[stone * 2024] += count
            stones[stone] -= count

print(sum(stones.values()))