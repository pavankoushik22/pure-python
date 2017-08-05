from stacks.stack import Stack


stk = Stack()


def recursive_push(s, i):
    if i != len(s):
        stk.push(s[i])
        i += 1
        recursive_push(s, i)


def recursive_pop(s):
    if not stk.is_empty():
        print(stk.peek(),end='')
        stk.pop()
        recursive_pop(s)

x = input('enter the string: ')
recursive_push(x, 0)
recursive_pop(x)
