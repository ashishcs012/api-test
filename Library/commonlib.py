class A:

    def __init__(self):
        print("this is class under class A constructor")

    def browserA(self):
        print("this is browser A")


class B:

    def __init__(self):
        print("this is class under class A constructor")

    def browserB(self):
        print("this is browser A")


obj = A()

obj.browserA()