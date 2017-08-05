from stacks.stack import Stack

stk = Stack()


def sort_insert(s, ele):
    if s.is_empty() or s.peek() <= ele:
        s.push(ele)
    else:
        temp = s.peek()
        s.pop()
        sort_insert(s, ele)


def sort_stack(ss):
    if not ss.is_empty():
        temp = ss.peek()
        ss.pop()
        sort_stack(ss)
        sort_insert(ss, temp)

for i in range(5):
    xx = int(input('enter number: '))
    stk.push(xx)

sort_stack(stk)

print(stk.size())
while not stk.is_empty():
    print(stk.peek(), end='')
    stk.pop()






