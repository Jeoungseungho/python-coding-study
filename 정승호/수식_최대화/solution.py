def calculate(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n]=='*':
        res = eval('*'.join([calculate(priority, n+1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calculate(priority, n + 1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calculate(priority, n + 1, e) for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]
    for priority in priorities:
        res = int(calculate(priority, 0, expression))
        answer = max(answer, abs(res))
    
    return answer
