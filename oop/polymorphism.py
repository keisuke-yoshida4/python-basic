class MyClass:
    def __str__(self):
        return "MyClassの__str__"


# mc = MyClass()
# print(mc)
# print(1)
# print("1")
# print(True)
# print([1, 2, 3])

def printvalue(arg):
    print(arg + 1)

printvalue(True)

various_types = [1, "1", True, [1, 2, 3], (1,), {'1': 1}, {1}]
# for elem in various_types:
#     print(elem)
