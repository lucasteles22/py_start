from folder.my_class import MyClass

print("###### instance method")
b = MyClass("Attr")
b.bar()
print("")

print("###### class method")
MyClass.foo()
print("")

print("###### static method")
MyClass.another()
