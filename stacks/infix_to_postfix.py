# infix to postfix conversion algorithm using stack.

from stacks.stack import Stack


def infix_to_postfix(s):
    operators = {'[': 0, '(': 0, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    stk = Stack()
    if len(s) == 0:
        return True
    for i in s:
        if i not in operators:
            print(i, end='')
        elif i == ')' or i == ']':
            while stk.peek() != '(' or stk.peek() != '[':
                print(stk.peek(), end='')
                stk.pop()
            stk.pop()
        else:
            while not stk.is_empty() and operators[i] <= operators[stk.peek()]:
                print(stk.peek(), end='')
                stk.pop()
            stk.push(i)
    while not stk.is_empty():
        print(stk.peek(), end='')
        stk.pop()
p = input('enter your string for conversion: ')
infix_to_postfix(p)
