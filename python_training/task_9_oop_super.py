class A:
    def __init__(self):
        self.x = 10
class B(A):

    def __init__(self):
        super().__init__()
        self.y = self.x + 10

b = B()
print(b.x)
print(b.y)