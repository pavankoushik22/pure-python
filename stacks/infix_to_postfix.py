# infix to postfix conversion algorithm using stack.

from stacks.stack import Stack


def infix_to_postfix(s):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    ops = ['+', '-', '*', '/', '^', '(', ')']
    stk = Stack()
    if len(s) == 0:
        return True
    for i in s:
        # if i is an operand
        if i not in ops:
            print(i, end='')
        elif i == '(':
            print('entered this too')
            stk.push(i)
        # pop until stack is empty or open parenthesis confronts
        elif i == ')':
            print('it entered this loop')
            while not stk.is_empty() and stk.peek() != '(':
                print(stk.peek(), end='')
                stk.pop()
            if not stk.is_empty():
                stk.pop()
        # an operand occurs then search for precedence
        else:
            while not stk.is_empty() and (stk.peek() == '(' or operators[i] <= operators[stk.peek()]):
                print(stk.peek(), end='')
                stk.pop()
            stk.push(i)
    while not stk.is_empty():
        print(stk.peek(), end='')
        stk.pop()
p = input('enter your string for conversion: ')
infix_to_postfix(p)
