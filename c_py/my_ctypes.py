from ctypes import CDLL, c_double, POINTER, c_int
# using ctypes
# c defaults in ctypes: argumnet types are int and char *
# return type is int by default

# non-default types
# func.argtypes, func.restype, POINTER(ctype)
mylib = CDLL("./mylib.so")

# mult
# enforce the argument types for mult
mylib.mult.argtypes = (c_double, c_double)

#enforce return type for mult
mylib.mult.restype = c_double

# call
print(mylib.mult(2.5, 3.5))  # ok
print(mylib.mult(2, 3))      # ok (probably coerces as int)

#print(mylib.mult('2', '3'))  # err
#print(mylib.mult(b'2', b'3'))# err

# divide
# note the POINTER being used to wrap the c_int for int *
mylib.divide.argtyps = (c_int, c_int, POINTER(c_int))
mylib.divide.restype = c_double

# call
remainder = c_int()  # assign a POINTER(c_int)

res =  mylib.divide(5, 4, remainder)  # ok
print("res: %f" % res, "remainder: %d" % remainder.value)

# avg (array)
mylib.avg.argtypes = (POINTER(c_double), c_int) # takes an array of doubles and the length as an int
mylib.avg.restype = c_double

def avg(seq):
  size = len(seq)
  arr = (c_double * size)
  print("arr = (c_double * %d) returns a callable" % size)
  print("callable(arr) = %s" % str(callable(arr)))
  print("types(arr) = %s" % str(type(arr)))

  #init the array (does not mutate so need to re-assign)
  #arr(*seq)
  arr = arr(*seq)
  print("called on input *seq: arr(*seq)")
  print("type(arr) = %s" % str(type(arr)))
  return mylib.avg(arr, size)

print(avg([x/2 for x in range(10)]))  # err floats reqired

# pointers
# use byref (only usable for args to fns)
from ctypes import byref, pointer
dval = c_double(0.0)                     # create a c double
result = mylib.show_double(byref(dval))  # show_double(&dval)

dval = c_double(2100.938746383387483202) # create a c double
result = mylib.show_double(byref(dval))  # show_double(&dval)

# or you can use pointer(), POINTER is for specifying types
ptr = pointer(dval)                      # get a pointer to instance
result = mylib.show_double(ptr)          # pass as pointer to dval

# strings
from ctypes import create_string_buffer, c_char_p, c_char
def replace(string, oldch, newch):
  sbuf = create_string_buffer(string)
  nrep = mylib.replace(sbuf, oldch, newch)
  return (sbuf.value, nrep)

#mystr = "radar"   # type error... unicode
mystr = 'radar'.encode('utf-8')
# 114 is 'r' and 109 is 'm'
mystr, num = replace(mystr, c_char(114), c_char(109))
#mystr, num = replace(mystr, "r", "m")  # this wont work since they are unicode
#                                       # calling "r".encode('utf-8') or b'r' doesn't work either...
print("Number of changes = %s" % num)
print(mystr)

# structs
from ctypes import Structure

class Point(Structure):
  _fields_ = [
    ("x", c_double),
    ("y", c_double)
  ]

# double slope(Point *p1, Point *p2)
mylib.slope.argtypes = (POINTER(Point), POINTER(Point))
mylib.slope.restype = c_double

# double slope2(Point p1, Point p2)
mylib.slope2.argtypes = (Point, Point)
mylib.slope2.restype = c_double

# instantiate
p1 = Point(1000, 2434)
p2 = Point(90, 99)

# can access the fields with dot notation
print("p1 (%f, %f)" % (p1.x, p1.y))
print("p2 (%f, %f)" % (p2.x, p2.y))

# all work!
print("slope: %f" % mylib.slope(p1, p2))
print("slope: %f" % mylib.slope(pointer(p1), pointer(p2)))
print("slope: %f" % mylib.slope(byref(p1), byref(p2)))

print("slope: %f" % mylib.slope2(p1, p2))
#print("slope: %f" % mylib.slope2(pointer(p1), pointer(p2)))  # TypeError
#print("slope: %f" % mylib.slope2(byref(p1), byref(p2)))      # Segmentation Fault!

# self-referential structs
class Node(Structure):
  pass

 # this method can be used but the print doesnt get called, should use another name and return self.val
 # actually, this should be calling itself recursively...
 # @property
 # def val(self):
 #   print("getter")
 #   return self.val

  def __str__(self):
    if (bool(self.left) and bool(self.right)):
      return "[%f]\n\t[left: %f][right: %f]" % (self.val, self.left.contents.val, self.right.contents.val)
    elif bool(self.left):
      return "[%f]\n\t[left: %f][_]" % (self.val, self.left.contents.val)
    elif bool(self.right):
      return "[%f]\n\t[_][right: %f]" % (self.val, self.right.contents.val)
    else:
      return "[%f]\n\t[_][_]" % self.val

Node._fields_ = [('val', c_double),
                ('left', POINTER(Node)),
                ('right', POINTER(Node))]

x = Node(9999.1)
y = Node(22293.222)

print(type(x))
print(type(x.val))
print(type(x.left))

# pointers have a contents attribute that is like * or ->
# bool(NULL pointers) evaluates to False

print(bool(x))               # TRUE
print(bool(x.left))          # FALSE
#print(bool(x.left.contents)) # Value Error: NULL pointer access

print(x.val)

# assemble the Nodes!
z = Node(100.0001)
z.left = pointer(x)
z.right = pointer(y)

print(x)
print(y)
print(z)

# you can nest Structs, notice that there is no Cherry struct defined in myfuncs.c
# python doesn't care if it exists or not in the .c file
# if a c function is actually going to use, it has to compile it first
class Cherry(Structure):
  _fields_ = [('parent', POINTER(Node)), ('left', POINTER(Node)), ('right', POINTER(Node))]

c = Cherry(pointer(z), pointer(x), pointer(y))

print(c.left.contents)
print(c.right.contents)
print(c.parent.contents)

# fields of the struct can be retrieved from the class
print(Cherry.parent)
print(Node.val)

# Structure (and Union) is really just used in python to express 
# such C structs (unions) in python.
# a function in C that relies on them can be called from python and passed these structs
# the C function will use them as the structs defined in the C file however...
mylib.show_cherry(pointer(c))
# this will print 0.000...
# so beware of what you are doing on both sides....
