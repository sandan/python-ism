# generators
# uses yield
# usually used to produce a sequence of values in iteration
# upon calling next() on generator, execution will continue until yield is reached
# can invoke next() with for, sum(), etc...

# instantiates a function that it calls, you get an object and you can call next()

def f(num):

  print(num)

  while(num):
    yield num
    num = num - 1
    print("after yield: num is now = %s" % str(num))

gen = f(19)
next(gen)
next(gen)

# you don't go to the yield until you call next()

# coroutines
# fn uses assignment (=) with yield keyword
# allows you to pass the generator with new state

def gen():
  while True:
    line = yield  # receive
    print(line)

s = gen()
next(s)  # advance to the yield inside the loop

s.send("hello")
s.send("world")
s.send("!")
s.close()


# can write decorators to instantiate coroutines to do:
# s = gen(*args, **kwargs)
# next(s)
#

# x = yield <-> receiver
# x = yield y <-> sender and receiver

# coroutines decouple data and function execution
def coru(*args, **kw):
# the args and kw passed can be used to modify execution
  result = None
  while True:
    # line is the args sent via send()
    line = yield result  # receive and send result back
    result = type(line)

s = coru()
next(s)

res = s.send(10)
print(res)

res = s.send("string")
print(res)

res = s.send(10.2)
print(res)

# kind of blends OO with functional...


# by advancing many separate generators
# in lock step, they will all seem to be
# running simultaneously (like threads executing
# and being interrupted after their time slice is up)
# this emulates the concurrent behavior of Python threads

# game of life
ALIVE = '*'
EMPTY = '-'
