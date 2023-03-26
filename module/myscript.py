# import mymodule
import sys
sys.path.append("/Users/keisuke/Desktop/PythonLecture/function")
import docstring

from mymodule import myfunc, myvariable
myfunc()
print(myvariable)
# print(mymodule.myvariable)

print(sys.path)
print(docstring.multiply(3, 4))

