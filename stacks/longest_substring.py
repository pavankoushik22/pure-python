from stacks.stack import Stack


def find_max_len(string):
    stk = Stack()
    stk.push(-1)
    result = 0
    for i in range(len(string)):
        if string[i] == '(':
            stk.push(i)
        else:
            stk.pop()
            if stk.is_empty():
                stk.push(string[i])
            else:
                result = max(result, i - stk.peek())
    return result


print(find_max_len('((()()'))
