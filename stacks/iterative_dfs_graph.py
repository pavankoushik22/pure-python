from stacks.stack import Stack


class Graph:
    v = None
    stk = Stack()

    def __init__(self, data):
        self.v = data
        self.b = [False] * data
        self.adj = [[]] * data

    def add_branch(self, i, j):

        self.adj[i].append(j)

    def dfs(self, source):
        self.stk.push(source)

        while not self.stk.is_empty():
            temp = self.stk.peek()
            self.stk.pop()
            if not self.b[temp]:
                self.b[temp] = True
                print(temp, end='')
            for i in self.adj[temp]:
                if not self.b[i]:
                    self.stk.push(i)

g = Graph(5)
g.add_branch(1, 0)
g.add_branch(0, 2)
g.add_branch(2, 1)
g.add_branch(0, 3)
g.add_branch(1, 4)
g.dfs(0)