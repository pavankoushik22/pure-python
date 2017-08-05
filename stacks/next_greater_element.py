from stacks.stack import Stack
dic = {}


def nge(lis):
    stk = Stack()
    print(lis)
    stk.push(lis[0])
    for i in lis[1:]:
        if not stk.is_empty():
            element = stk.peek()
            stk.pop()
            while element < i:
                print('%d ---- %d'%(element, i))
                if stk.is_empty():
                    break
                element = stk.peek()
                stk.pop()
            if element > i:
                stk.push(element)
        stk.push(i)

    while not stk.is_empty():
        print('%d --- %d'%(stk.peek(), -1))
        stk.pop()


a = list(map(int, input('enter the array: ').split(' ')))

nge(a)



