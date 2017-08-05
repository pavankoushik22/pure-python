from stacks.stack import Stack


def evaluator(s):
    index = 0
    operators = {'[': 0, '(': 0, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    temp = []
    for i in s:
        if i not in s:
            temp.append(i)
        elif i != '(' or i != '[' or i != ']' or i != ')':
            index = index + eval(temp[0]+)
