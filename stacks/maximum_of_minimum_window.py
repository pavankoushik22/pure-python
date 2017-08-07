from stacks.stack import Stack

x = list(map(int, input().split(' ')))

stk = Stack()
stk1 = Stack()
left = [-1]*len(x)
right = [len(x)]*len(x)

# for filling left array

for i in range(len(x)):
    while not stk.is_empty() and x[stk.peek()] >= x[i]:
        stk.pop()
    if not stk.is_empty():
        left[i] = stk.peek()
    stk.push(i)

# for filling right array

for j in range(len(x)-1, -1, -1):
    while not stk1.is_empty() and x[stk1.peek()] >= x[j]:
        stk1.pop()
    if not stk1.is_empty():
        right[j] = stk1.peek()
    stk1.push(j)

ans = [0]*(len(x)+1)

for k in range(len(x)):
    length = right[k] - left[k] - 1
    ans[length] = max(ans[length], x[k])

# for windows sizes that not filled


for l in range(len(x)-1, -1, -1):
    ans[l] = max(ans[l], ans[l+1])

print(ans[1:])

