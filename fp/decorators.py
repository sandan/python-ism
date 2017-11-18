# decorators 
# - start with @
# - wraps another function or class
# - closures implement decorators
# 3 things you can decorate:
# - global fn, method in a class, class
# decorators usually stored in modules and imported
# - useful for checking args of funcs/pre-processing
# using *args and *kw is useful here too
# good for refactoring:
# - you only change the function in one place to affect everywhere it is called
# ( no need to wrap the function with another function in all places to modify its behavior)
# no need to change the internal body of the function - good for writing code ancilliary to the fn's purpose (error handling, logging, arg processing, etc.)
# can replace functions totally - acting as a shim - made explicit by @


# a cache decorator around a fn
def cache(fn):

  s = dict()
  print("inside cache")
  def inner(arg_to_fn):
    if arg_to_fn in s:
      return s[arg_to_fn]
    else:
      res = fn(arg_to_fn)
      s[arg_to_fn] = res
      return res

  return inner

@cache
def fib(n):
  # returns the nth factorial

  if (n  == 0):
    return 1
  else:
    return fib(n-1) + n

# equivalent to the assignment when decorator is applied
# fibonacci = cache(fibonacci)
# passes reference to the function you are decorating

print(fib(5))

# you can decorate a decorator
def decked(fn):
  def inner(arg_to_fn):
    print("inside decked!")
    return fn(arg_to_fn)
  return inner

# you can apply multiple decorators in python
# the one closest to the function being decorated executes sooner

@decked
@cache
def factorial(n):
  if (n == 0):
    return 1
  else:
    return n * factorial(n-1)
# equivalent to:
# factorial = decked(cache(factorial))

print(factorial(5))

# decorators get recalled on recursive calls!

# apply @wraps from functools
# - propagates function name and other metadata belonging to the decorated fn (like name and docstrings)
# - needed for having multiple args (*args, *kwargs)?
# - decorates the inner function that usually calls the fn that is actually being decorated

from functools import wraps
from time import time
def decked3(fn):
  @wraps(fn)
  def inner(args_to_fn):
    print("inside decked3 with args: %s" % args_to_fn)
  return inner

@decked3
def g(x):
  return 2 * x
print(g.__name__) # allowed bc of @wraps o/w would be decorator's name
print(g(2))


# decorator arguments
# equivalently like this when they have args
# parameterized decorators are decorator factories - they produce decorators

def decked2(arg):
  def inner(fn):
    print(arg)
    return fn  # looks like you lose the args to fn tho...
  return inner

@decked2("decked_arg1")
def f(x):
  return x + 1

# equivalently:
# temp = decked2("decked_arg1")
# f = temp(f)

print(f(99))  # .. but the function still gets called with its arg -> prints 100

# you can wrap the decorator to allow for more args
def dec(x, y, z):
  def actual_dec(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
      print(x, y, z)
      return fn(*args, **kwargs)
    return inner
  return actual_dec

@dec("hello", "world", "!")
def h(p, q):
  return p + 2 + q

print(h(20, 99))

# or just use two levels and return the function (w/o calling it):
def dec2(x, y, z):
  def actual_dec(fn):
    print(x, y, z)
    return fn
  return actual_dec

@dec2("hello", "universe", "!")
def h(l):
  return l + 10

print(h(1000))
print(h.__name__) # note that @wraps isnt needed...

def d(a, **kw):
  print("d")
  def dec(fn):
    print("d : dec", fn.__name__) # fn name is t (because of @wraps)
    @wraps(fn)
    def inner(*args, **kwargs):
      print("d : inner")
      kwargs["d"] = a
      return fn(*args, **kwargs)
    return inner
  return dec

def e(a, b, **kw):
  print("e")
  def dec(fn):
    print("e : dec", fn.__name__) # fn name is t
    @wraps(fn)
    def inner(*args, **kwargs):
      print("e : inner", 'd' in kwargs)
      kwargs["e"] = [a, b]
      return fn(*args, **kwargs)
    return inner
  return dec

# can I generalize the dec/inner of both e,d above?
print()
@d("this is d's argument")
@e("this is e", "this is e again")
def t(x, **kw):

  if 'd' in kw:
    print("got args from d: ", kw['d'])
  if 'e' in kw:
    print("got args from e: ", kw['e'])

  return x + 1

print("=======================================")
print(t(99))
print("=======================================")


# parameterization happens from the outside (farther away from decorated fn) in (towards the decorated fn)
# temp1 = d("this is d's argument")         --> prints "d"
# temp2 = e("this is e", "this is e again") --> prints "e"

# ... so now we have ...
# @temp1
# @temp2
# def t(x, **kw) ...

# ... so this translates to ...
# t = temp1(temp2(t))           --> prints "e : dec" then prints "d : dec"

# note that the previous prints for this example occur separately from the actual invocation of the function t()
# try commenting out print(t(99))
# t(99)                         --> prints "d : inner" then prints "e : inner" 

# d
# e
# e : dec
# d : dec
# d : inner
# e : inner

# so heres a step-by-step
# 1) parameterized decorator temp1 returns a decorator (returns d.dec)
# 2) parameterized decorator temp2 returns a decorator (returns e.dec)
# 3) t is redecorated with the resulting decorators, this is equivalent to t = temp1(temp2(t))
# 4) temp2(t) is evaluated with the function object t e.dec gets called with fn = t and returns e.dec.inner
# 5) temp1(e.dec.inner) is evaluated with function object e.dec.inner with the fn in e.dec.inner referring to t
# 6) now the fn in d.dec.inner is e.dec.inner, this is where the @wraps is useful
# 7) @wraps decorates e.dec.inner this makes the fn.__name__ = to t
#    fn in d.dec.inner is not t but is actually still e.dec.inner,
#    only the __name__ (and other attributes) get affected not the actual func object
#    (to prove this, check kwargs in e.dec.inner to see that d has added stuff to it). print("e : inner", 'd' in kwargs) will print T
#
#    @wraps propagates info about fn which is t in e.dec.inner to d.dec.inner
#    (rename e.dec.inner to e.dec.e_inner and comment out the @wraps of e_inner to see proof, this prevents t from being propagated up)
# 8) so finally we have t = d.dec.inner
# 9) when t(99) is called d.dec.inner runs and calls -> e.dec.inner which calls -> t (add kwargs on the way)


# ... and again without using the wrappers for the dec args ...
def q(a, **kw):
  print("q", a)
  def dec(fn):
    print("q : dec")
    return fn
  return dec

def r(a, b, **kw):
  print("r", a, b)
  def dec(fn):
    print("r : dec")
    return fn
  return dec

print()
@q("q !")
@r("r !", "r !!")
def t2(x):
  return x + 1

print(t2(3))
# but can't affect the kw of fn...
# use this pattern when the args to the fn dont matter
# tmp1 = q("q !")           --> prints "q q !"
# tmp2 = r("r !", "r !!")   --> prints "r r ! r !!"
# 
#... so this will be like...
# @tmp1
# @tmp2
# def t2(x): ...
#
#... so this should be like...
# t2 = tmp1(tmp2(t2))

# print output:
# q  
# r
# r : dec
# q : dec

# so t2(3) is really tmp1(tmp2(t2(3)))
print()

def x1(arg1, **kw):
  print("x1")
  def a(fn):
    print("x1 : a")
    @wraps(fn)
    def b(*args, **kwargs):
      print("x1 : b")
      def c(*args, **kwargs):
        print("x1 : c")
        return fn(*args, **kwargs)
      return c
    return b
  return a

def x2(arg1, **kw):
  print("x2")
  def a(fn):
    print("x2 : a")
    @wraps(fn)
    def b(*args, **kwargs):
      print("x2 : b")
      def c(*args, **kwargs):
        print("x2 : c")
        return fn(*args, **kwargs)
      return c
    return b
  return a

@x1("x1 arg")
def f1(x):
  return type(x)

print(f1(99))
print()
# temp = x1("x1 arg")
# f1 = temp(f1)

# @temp
# def f1() ...

#...or...
# f1 = a(f1)
# f1 = b at this point
# calling f1(99) returns a function c ...

# this pattern allows you to write a function that takes a function and allows you to call
res = f1(sum)([x**2 for x in range(20)]) # call sum with args in the list
print(res)

# so basically you can do:
# f1(func)(func args) for certain behavior
# or
# f1(args) for another behavior

# the typical depth of the decorator closures is probably 3...
# outermost for the args to parametrize the dec
# the middle that is the actual dec
# the inner for wrapping the decorated func

