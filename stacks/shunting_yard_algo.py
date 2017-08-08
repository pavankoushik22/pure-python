from stacks.stack import Stack

valueStk = Stack()
opStk = Stack()
ops = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
x = input('enter your expression: ')
dump = ['{', '}']
for i in x:
    if i not in ops and i not in dump:
        valueStk.push(int(i))
    elif i == '{':
        opStk.push(i)
    elif i == '}':
        while not opStk.is_empty() and opStk.peek() != '{':
            a = valueStk.peek()
            valueStk.pop()
            b = valueStk.peek()
            valueStk.pop()
            ops = opStk.peek()
            opStk.pop()
            temp = str(b) + ops + str(a)
            result = eval(temp)
            valueStk.push(result)
        if not opStk.is_empty():
            opStk.pop()
    elif i in ops:
        while not opStk.is_empty() and opStk.peek() != '{' and ops[opStk.peek()] >= ops[i]:
            a = valueStk.peek()
            valueStk.pop()
            b = valueStk.peek()
            valueStk.pop()
            ops = opStk.peek()
            opStk.pop()
            temp = str(b) + ops + str(a)
            result = eval(temp)
            valueStk.push(result)
        opStk.push(i)

while not opStk.is_empty() and not valueStk.is_empty():
    a = valueStk.peek()
    valueStk.pop()
    b = valueStk.peek()
    valueStk.pop()
    ops = opStk.peek()
    opStk.pop()
    temp = str(b) + str(ops) + str(a)
    result = eval(temp)
    valueStk.push(result)
print(valueStk.peek())
