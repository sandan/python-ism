#!/Users/ms186122/anaconda/bin
from ctypes import CDLL, c_char_p

mylib = CDLL("./mylib.so")
print(type(mylib))

# call funcs from lib
print(type(mylib.greeting))
print(type(mylib.add(2, 3)))

# call from python
res1 = mylib.greeting("bob") # return code 0
mylib.greeting("abc")        # 'b' and 'a' are printed bc they are unicode, null terminator is reached in c printf
res2 = mylib.add(99, 1)      # 100
print(res1, res2)

# encode the string as a byte string
mylib.greeting(b"abc")

# or tell ctypes about the right param type
printf = mylib.printf
printf.argtypes = [c_char_p]
printf("testing...\n")

# this will cause an error:
#  File "invoke.py", line 23, in <module>
#    printf("testing...\n")
#    ctypes.ArgumentError: argument 1: <class 'TypeError'>: wrong type
# the type passed is still wchar...

# notice you can also use a variable to reference the function pointer
