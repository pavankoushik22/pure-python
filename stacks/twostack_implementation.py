# two stack in one array implementation


class TwoStack:
    main = [0]*20
    l = 0
    r = 19

    def push1(self, s):
        self.main[self.l] = s
        self.l += 1

    def push2(self, s):
        self.main[self.r] = s
        self.r += 1

    def pop1(self):
        if self.l != 0:
            self.l = self.l - 1
            print(self.main[self.l])
            return self.main[self.l]

    def pop2(self):
        if self.r != 0:
            self.r = self.r + 1
            print(self.main[self.r])
            return self.main[self.r]

stk = TwoStack()
while True:
    temp = input('enter the query: ')
    x = temp.split(' ')
    # if it is push
    if len(x) == 3:
        if x[1] == '1':
            stk.push1(x[2])
        else:
            stk.push2(x[2])
    else:
        if x[1] == '1':
            stk.pop1()
        else:
            stk.pop2()
