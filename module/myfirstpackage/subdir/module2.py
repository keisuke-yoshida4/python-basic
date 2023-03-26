# from .module3 import myfunc3
# from ..import module1
from ..module1 import myfunc as module1_func


def myfunc():
    print("This is myfunc from module2")


def myfunc2():
    print("this is my func2 from module2")
    module1_func()
