import re

def multiply(a, b):
    return a * b

with open('input.txt') as f:
    data = f.read()

pattern = r"mul\((\d+),\s*(\d+)\)"
uncorrupted_data = re.findall(pattern, data)
sum = 0
for i in uncorrupted_data:
    sum += multiply(int(i[0]), int(i[1]))

print(sum)
