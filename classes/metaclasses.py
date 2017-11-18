# Metaclasses
# - an object that knows how to create and manage classes
# - Lets you intercept class statements and customize behaviors
# - configuring a class dynamically
# - hooks: new(), init(), call()
# - __new__ - called before class is parsed (defined)
# - __init__ - called after class is parsed (defined)
# - __call__ - called before constructor is called
# metaclasses inherit from type
# metaclasses dont get instantiated

class t(type):
  def __new__(cls, *args, **kw):
    print("t : new")  # gets run at import time (before class is defined)
    return super().__new__(cls, *args, **kw)

  def __init__(self, *args, **kw):
    print("t : init") # gets run at import time (after class is defined)
    super().__init__(*args, **kw)

  def __call__(self):
    print("t : call") # gets called before __init__ executes in s
    super().__call__()

class s(object, metaclass=t):  # changed in py3.5
  # __metaclass__ = t  # attach a metaclass to your class
  def __init__(self):
    print("s constructor")   # runs after __call__ in metaclass

# when you use s, the metaclass t will intercept the class s
# the hooks explained are as above (new, init, call)
# the signatures for Py3 and Py2 are different for new and init

# implementation of a singleton
calss singleton(type):
  def __init__(self, *args, **kw):
    print("singleton : __init__")
    super().__init__(*args, **kw)
