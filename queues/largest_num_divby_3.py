from queues.queue import Queue

lis = list(map(int, input().split(' ')))
lis.sort()
n = len(lis)
q1 = Queue(n)
q2 = Queue(n)
q3 = Queue(n)
total = sum(lis)
for i in lis:
    if i%3 == 0:
        q1.enqueue(i)
    elif i%3 == 1:
        q2.enqueue(i)
    else:
        q3.enqueue(i)
if total%3 == 1:
    if not q2.is_empty():
        q2.dqueue()
    else:
        q3.dqueue()
        q3.dqueue()
elif total%3 == 2:
    if not q3.is_empty():
        q3.dqueue()
    else:
        q2.dqueue()
        q2.dqueue()
else:
    print(lis)

newl = []
while not q1.is_empty():
    newl.append(q1.dqueue())
while not q2.is_empty():
    newl.append(q2.dqueue())
while not q3.is_empty():
    newl.append(q3.dqueue())
newl.sort(reverse= True)
print(newl)
