from stacks.stack import Stack

tp = None
stk = Stack()
x = list(map(int, input().split(' ')))
n = len(x)
i = 0
maxi = 0
while (i < n):
    if stk.is_empty() or x[stk.peek()] <= x[i]:
        stk.push(i)
        i += 1

    else:
        tp = stk.peek()
        stk.pop()
        if stk.is_empty():
            temp = x[tp] * i
        else:
            temp = x[tp] * (i - stk.peek() - 1)
        if maxi < temp:
            maxi = temp
while not stk.is_empty():
    tp = stk.peek()
    stk.pop()
    if stk.is_empty():
        temp = x[tp] * i
    else:

        temp = x[tp] * (i - stk.peek() - 1)
    if maxi < temp:
        print(maxi)
        maxi = temp

print(maxi)
