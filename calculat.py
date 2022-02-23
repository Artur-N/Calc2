def calculation(x, y, op):
    if op == '+':
        res = x + y
    if op == '-':
        res = x - y
    if op == '*':
        res = x * y
    if op == '/':
        res = round(x / y, 2)
    return res

