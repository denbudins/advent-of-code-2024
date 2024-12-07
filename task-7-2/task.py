import itertools

with open('input.txt') as f:
    data = f.read().split('\n')

operators = ['+', '*', '||']
allCorrectEquationsResults = []


for equation in data:
    equationResults = equation.split(':')[0]
    equationNumbers = equation.split(':')[1].split()
    operator_combinations = itertools.product(operators, repeat=len(equationNumbers) - 1)
    for operator_set in operator_combinations:
        copyOfEquationNumbers = equationNumbers.copy()
        result = 0
        for i, operator in enumerate(operator_set):
            if operator == '||':
                if i == 0:
                    cobainNumbers = int(copyOfEquationNumbers[i] + copyOfEquationNumbers[i + 1])
                    copyOfEquationNumbers[i + 1] = str(cobainNumbers)
                    result = cobainNumbers
                else:
                    cobainNumbers = int(str(result) + copyOfEquationNumbers[i + 1])
                    copyOfEquationNumbers[i + 1] = str(cobainNumbers)
                result = cobainNumbers
                continue
            if i == 0:
                result = eval(copyOfEquationNumbers[i] + operator + copyOfEquationNumbers[i + 1])
            else:
                result = eval(str(result) + operator + copyOfEquationNumbers[i + 1])
        if result == int(equationResults):
            allCorrectEquationsResults.append(result)
            break

print(sum(allCorrectEquationsResults))