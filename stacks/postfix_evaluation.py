from stacks.stack import Stack


def evaluator(s):
    operators = {'[': 0, '(': 0, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

    stk = Stack()
    for i in s:
        if i not in operators:
            stk.push(i)
        else:
            temp = stk.peek()
            stk.pop()
            temp1 = stk.peek()
            stk.pop()
            final = temp1+i+temp
            fin = eval(final)
            stk.push(fin)
    if stk.size() == 1:
        print(stk.peek())
        stk.pop()
    else:
        print('not valid!')


x = input('enter the postfix string: ')
evaluator(x)
