##
# Abstract classes can have metaclasses
# This is useful for implementing the singleton pattern for an abstract class
##
from abc import ABC, ABCMeta, abstractmethod

class singleton(ABCMeta):
    """
    A generic metaclass for implementing the singleton pattern
    """
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._instance = None

    def __call__(self, *args, **kw):
        if self._instance is None:
            self._instance = super().__call__(*args, **kw)
        return self._instance

class abstract_thing(ABC, metaclass=singleton):

  @property
  @abstractmethod
  def my_abstract_property(self):
    pass

  @abstractmethod
  def __len__(self):
    pass

# class concrete_thing(abstract_thing, list):
#
# Order of inheritance matters when implementing abstract class
#  if list is subclassed after abstract_thing, __len__ will not be implemented
#  if list is subclassed first, list.__len__ implements abstract_thing.__len__
#
class concrete_thing1(list, abstract_thing):

  @property
  def my_abstract_property(self):
    return self._data

  @my_abstract_property.setter
  def my_abstract_property(self, val):
    self._data = val

class concrete_thing2(abstract_thing, list):

  @property
  def my_abstract_property(self):
    return self._data

  @my_abstract_property.setter
  def my_abstract_property(self, val):
    self._data = val


if __name__ == '__main__':

  c1 = concrete_thing1()
  c2 = concrete_thing2()

  print('list implements abstract methods when specified first: ', len(c1))
  try:
    print(len(c2))
  except TypeError:
    print('if subclassed after, throws err')
