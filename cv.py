class a:
    def __init__(self):
        print(f'생성 되면서 출력{self.name}')
    
    name = "a"

class b:
    def __init__(self):
        self.name = 'b'

class c:
    def __init__(self):
        self.name = "c"

class test(a):
    def __init__(self):
        super().__init__()
    
    def show(self):
        print(self.name)

test1 = test()
test1.show()