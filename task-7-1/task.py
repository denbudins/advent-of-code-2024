import itertools

with open('input.txt') as f:
    data = f.read().split('\n')

operators = ['+', '*']
allCorrectEquationsResults = []


for equation in data:
    equationResults = equation.split(':')[0]
    equationNumbers = equation.split(':')[1].split()
    operator_combinations = itertools.product(operators, repeat=len(equationNumbers) - 1)
    for operator_set in operator_combinations:
        result = 0
        for i, operator in enumerate(operator_set):
            if i == 0:
                result = eval(equationNumbers[i] + operator + equationNumbers[i + 1])
            else:
                result = eval(str(result) + operator + equationNumbers[i + 1])
        if result == int(equationResults):
            allCorrectEquationsResults.append(result)
            break

print(sum(allCorrectEquationsResults))