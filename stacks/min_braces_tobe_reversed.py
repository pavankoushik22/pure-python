from stacks.stack import Stack
import math

x = input('enter your string: ')
stk = Stack()
stk1 = Stack()
r = 0
l = 0
for i in x:
    if i == '{':
        l += 1
        stk.push(i)
    elif not stk.is_empty() and stk.peek() == '{':
        l = l - 1
        stk.pop()
    else:
        r += 1
        stk1.push(r)

print(math.ceil((r / 2)) + math.ceil(l / 2))
