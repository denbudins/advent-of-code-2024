with open('input.txt') as f:
    data = f.read().split('\n\n')

pageOrderingRules =  [red.split('|') for red in data[0].split('\n')]
pagesToProduce = [red.split(',') for red in data[1].split('\n')]
pagesInRightOrder = []

for i in pagesToProduce:
    pagesToProduceLength = len(i)
    inRightOrder = True
    for j in range(pagesToProduceLength):
        if j + 1 < pagesToProduceLength:
            for k in range(j + 1, pagesToProduceLength):
                result = next((pair for pair in pageOrderingRules if pair[0] == i[j] and pair[1] == i[k]), None)
                if result is None:
                    inRightOrder = False
                    break
        if not inRightOrder:
            break
    if inRightOrder:
        pagesInRightOrder.append(i)

middleElements = [int(pagesInRightOrder[len(pagesInRightOrder) // 2]) for pagesInRightOrder in pagesInRightOrder]
print(sum(middleElements))