class MyClass:
    thing = "athing"

    def __init__(self, attr):
        self.attr = attr

    # Instance method
    def bar(self):
        print(self.thing)
        print(self.attr)
        self.foo()
        self.another()

    # Class method
    @classmethod
    def foo(cls):
        print("foo")
        print(cls.thing)
        cls.another()

    # Static method
    @staticmethod
    def another():
        print("another")
