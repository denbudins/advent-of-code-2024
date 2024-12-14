with open('input.txt') as f:
    stones = f.read().split(' ')

numberOfBlinking = 25
for i in range(numberOfBlinking):
    blinking = []
    for stone in stones:
        numberOfDigits = len(str(stone))
        if int(stone) == 0:
            blinking.append(1)
        elif numberOfDigits % 2 == 0:
            numberOfDigitsEveryHalf = numberOfDigits // 2
            firstHalf = str(stone)[:numberOfDigitsEveryHalf]
            secundHalf = str(stone)[numberOfDigitsEveryHalf:]
            blinking.append(int(firstHalf))
            blinking.append(int(secundHalf))
        else:
            blinking.append(int(stone) * 2024)
    stones = blinking

print(len(stones))