import re

def multiply(a, b):
    return a * b

with open('input.txt') as f:
    data = f.read()

pattern = r"""(don't\(\))|(do\(\))|(mul\((\d+),(\d+)\))"""
uncorrupted_data = re.findall(pattern, data)

sum = 0
isRunning = True
for i in uncorrupted_data:
    if(i == ("", "do()", "", "", "")):
        isRunning = True
    elif(i == ("don't()", "" , "", "", "")):
        isRunning = False
    elif(isRunning):
        sum += multiply(int(i[3]), int(i[4]))

print(sum)
