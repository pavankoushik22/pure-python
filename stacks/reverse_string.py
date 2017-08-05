from stacks.stack import Stack


def reverse(string):
    stk = Stack()
    for i in string:
        stk.push(i)
    while not stk.is_empty():
        print(stk.peek(), end='')
        stk.pop()

reverse('pavankoushik')