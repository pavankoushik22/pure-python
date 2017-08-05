class SpecialStack:
    a = []
    b = []

    def push(self,i):
        self.a.append(i)
        if len(self.b) == 0 or i <= self.b[-1]:
            self.b.append(i)
        else:
            self.b.append(self.b[-1])

    def pop(self):
        self.b.pop()
        return self.a.pop()

    def get_min(self):
        return self.b[-1]

s = SpecialStack()
s.push(1)
s.push(2)
s.push(3)
s.push(1)
print(s.get_min())