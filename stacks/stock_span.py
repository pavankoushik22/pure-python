from stacks.stack import Stack
S = []


def stock_span(lis):
    stk = Stack()

    S.append(1)
    stk.push(0)
    for i in lis[1:]:
        while not stk.is_empty() and lis[stk.peek()] <= i:
            stk.pop()
        if stk.is_empty():
            S.append(lis.index(i)+1)
        else:

            S.append(lis.index(i) - stk.peek())
        stk.push(lis.index(i))

a = input('enter the stocks list: ')
aa = list(map(int, a.split(' ')))

stock_span(aa)
print(S)
