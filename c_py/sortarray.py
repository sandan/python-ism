from ctypes import CDLL, c_int, POINTER

mylib = CDLL("./mylib.so")
mylib.sortArray.argtypes = (c_int, POINTER(c_int))
#mylib.sortArray.restype = 

def sortArray(n):
  size = len(n)
  arr = (c_int * size)(*n)
  mylib.sortArray(size, arr)
  return arr

nums = [7, 0, 8, 4, 3, 6, 9, 1, 5, 2]
nums = sortArray(nums)
print(type(nums))
print(list(nums))
print(nums[:])
