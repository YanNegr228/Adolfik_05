class Parent1:
    def __init__(self):
        self.attribute1 = "Parent 1 Attribute"

    def method1(self):
        print("Parent 1 Method")


class Parent2:
    def __init__(self):
        self.attribute2 = "Parent 2 Attribute"

    def method2(self):
        print("Parent 2 Method")


class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()

    def child_method(self):
        print("Child Method")
        print(self.attribute1)
        print(self.attribute2)


child_obj = Child()
child_obj.child_method()
child_obj.method1()
child_obj.method2()
