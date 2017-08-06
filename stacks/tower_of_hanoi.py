from stacks.stack import Stack

A = Stack()
B = Stack()
C = Stack()

A.push(3)
A.push(2)
A.push(1)


def move_disks(src, aux, dest, n):
    if n == 0:
        return 0
    else:
        move_disks(src, dest, aux, n-1)
        temp = src.peek()
        print('moving %d from %s to %s ' % (temp, src, dest))
        dest.push(temp)
        src.pop()
        move_disks(aux, src, dest, n-1)

move_disks(A, B, C, 3)
print(C.peek())
C.pop()
print(C.peek())
C.pop()
print(C.peek())
C.pop()
