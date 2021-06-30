class a:
    def __init__(self):
        self.name = "a"

class b:
    def __init__(self):
        self.name = 'b'

class c:
    def __init__(self):
        self.name = "c"

class test(a,b,c):
    def __init__(self):
        super(a,self).__init__()
        print(super())

    
    def show(self):
        print(self.name)

test1 = test()