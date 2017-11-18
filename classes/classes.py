# new style class
# - inherits from object
# - may subclass most built-in types
# - descriptors + slots
# default in python 3.x

# stack implemented with a list
class stack(object):

  def __init__(self):
    self.__stack__ = []

  def push(self, data):
    self.__stack__.append(data)

  def pop(self):
    return self.__stack__.pop()

  def length(self):
    return len(self.__stack__)

  def is_empty(self):
    return len(self.__stack__) == 0

# you can inherit from any python built-in
class my_list(list):
  # access to list is self
  def __init__(self, items):
    super().__init__(items) # call super to init parent

  def append(self, val):  # override?
    print(type(self))
    print(self)
    # self.append(val) # this will infinitely recurse...
    self += [val]

  def nitems(self):  # extend
    counts = ()
    for item in self:
      counts.setdefault(item, 0)
      counts[item] += 1
    return counts

# diamond inheritance
# subclass inherits from two classes with the same superclass
# python will do 1 copy of the same (parent) superclass, 
# it's children (from left to right), 
# then finally the leaf

# parent
class machine(object):         # order of prints:
  def __init__(self):
    print("Machine constr")    # 4

# child
class phone(machine):
  def __init__(self):
    print("phone contsr 1")    # 2
    super().__init__()
    print("phone contsr 2")    # 6
# child
class computer(machine):
  def __init__(self):
    print("computer constr 1") # 3
    super().__init__()
    print("computer constr 2") # 5

# leaf
class smartphone(phone, computer):
  def __init__(self):
    print("smartphone 1")      # 1
    super().__init__()
    print("smartphone 2")      # 7

# property decorators

class circle(object):
  def __init__(self, init_radius = 1):
    self.radius = init_radius

  @property
  def radius(self):
    print("getting radius...")
    return self.__radius        # return a 'hidden' variable

  @radius.setter   # radius.setter is named with fn name that has corresponding @property
  def radius(self, new_radius):
    if (new_radius <= 0):
      raise ValueError("bad radius %d" %new_radius)
    self.__radius = new_radius  # set a 'hidden' variable

# c = circle(0) will throw an error - the setter is called in constructor
# c.radius invokes the @property which calls the function radius
# c.__radius does not exist...
# c._circle__radius does exist... and is the value when the getter is called

# slots
# __slots__ can only be assigned inside class
# - a tuple of allowable class attributes
# - if defined, exposes it as class.__slots__
# - variables in classes starting with _ are inherited from children - useful for default values
# - variables in classes starting with __
# - Class exposes defined attributes in __slots__
# - can be used to avoid monkey-patching when setting attributes
# class is managed by a dict, adding slots makes class managed by a tuple which is an array under the hood
# faster to look up an attribute in a slot (array- apparently linear) rather than dict (hashmap - apparently log time)
class polar(object):
  #__slots__ = ("radius", "theta", "__radius", "_polar__radius")
  __slots__ = ("inner_radius", "theta")
  def __init__(self, radius, theta):
    self.radius = radius
    self.theta = theta

  @property
  def radius(self):          # the method name can't be radius too since it conflicts with radius in slots
    print("getting radius")  # so change the slot name and set it
    return self.inner_radius   # notice we don't use __radius, o/w we get Attribute errors

  @radius.setter
  def radius(self, radius):
    print("setting radius")
    self.inner_radius = radius # notice we don't use __radius, o/w we get Attribute errors

# p = polar(10, 45)
# 'p.radus' -> gives errors on spelling err since it isn't defined
# 'p.radus' = 10 -> gives an error since 'radus' is not in slots
# if you comment out the slots attribute, you can't get but you can set (monkey patch)
# since python duck types classes
# why do we use __ in properties? They are private variables in python, used to signify not to expose to user
