# closures 
#  - returns a reference to another function (inner function)
#  - the inner function is created inside the function
#  - captures state in execution environment
#  - used to implement streams, iterators
#  - (1) def inside of a def and (2) outer def returns inner def name

def f():
  x = 42
  def inner():
    print(x)
  return inner

outer = f()
print(outer())

# the outer function is used to construct the state
# about how to execute the inner function


from time import time, sleep

def timestamp():
  start = time()
  def inner():
    return time() - start
  return (inner, start)

stamp, start = timestamp()
print(stamp())
sleep(3)
print(stamp())

# inner fn could also be a lambda
# can't access the inner fn anyway

def outer():
  x = 90
  return lambda : print(x)

anon = outer()
print(anon())

# closures can be used to implement factories
# private variables

