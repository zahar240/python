"""Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2"""

expressions = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]

for expression in expressions:
    print(type(expression))