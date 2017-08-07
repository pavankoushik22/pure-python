from stacks.stack import Stack
x = list(map(int, input('enter the elements: ').split(' ')))
mini = 0
stk = Stack()

root = mini
for i in x:
    if i < root:
        print('can not be a pre order ')
        break
    while not stk.is_empty() and stk.peek() < i:
        root = stk.peek()
        stk.pop()
    stk.push(i)
