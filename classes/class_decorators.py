# class decorator
# wraps the class definition
# follows same idiom c = f(c)
# @f
# class c(...
# customize class definition
# can be paremeterized and have multiple decs

registry = {} # gets populated during import time, not instantiation time of c

def f(cls):
  print("f")  # this gets printed when you import * from this module
  registry[cls.__name__] = cls
  return cls

@f
class c(object):
  def __init__(self):
    print("c constructor")

# c = f(c)
# now when we call c, we don't print f

# method decorators
# function wrapping a class method
# can be paremeterized and have multiple args
# may be applied to instance, class, and static methods
from functools import wraps

def g(fn):
  print("g", fn.__name__)   # happens at import time
  @wraps(fn)
  def inner(*args, **kwargs):
    print("g : inner")      # happens when constructor function is called
    return fn(*args, **kwargs)
  return inner

class d(object):
  @g
  def __init__(self):
    print("d constructor")


