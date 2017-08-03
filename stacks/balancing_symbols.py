
# using stacks for checking balancing of symbols.

from .stack import Stack


def is_valid_symbol(s):
    stk = Stack()
    if len(s) == 0:
        return True
    for i in s:
        if i == ']' or i == '}' or i == ')':
            if stk.is_empty():
                return False
            else:
                stk.pop()
        else:
            stk.push(i)
    if stk.is_empty():
        return True
    else:
        return False


x = input('Enter the string that has to verified: ')
print(is_valid_symbol(x))
