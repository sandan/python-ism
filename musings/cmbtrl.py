
def add_coru(a, b):
  yield a + b

adder = add_coru(1, 2)
x = next(adder)
print(x)

try:
  next(adder)
except StopIteration:
  print("calling next(adder) again causes a StopIteration")

# fib
def fib():
  a, b = 0, 1
  while True:
    yield b  # yields the nth fib number on nth next() call
    a, b = b, a + b

f = fib()
for times in range(10):
  # 1st 10 fib numbers
  print(next(f))

# recursive generators
# recursive algorithm implemented using coroutines
# generators will call next inside the fn again till key DNE (tree['left'] or tree['right'] doesnt exist )
from collections import defaultdict

# post order traversal of binary tree implemented as a nested dict
def postorder(tree):
  if not tree:
    return

  for x in postorder(tree['left']):
    yield x

  for x in postorder(tree['right']):
    yield x

  yield tree['value']

# equivalent to above but with py3 syntax
def postorder2(T):
  if not T:
    return

  yield from postorder(T['left'])
  yield from postorder(T['right'])
  yield T['value']


# preorder
def preorder(T):
  if not T:
    return

  yield T['value']

  for x in preorder(T['left']):
    yield x

  for x in preorder(T['right']):
    yield x

# inorder
def inorder(T):
  if not T:
    return

  for x in inorder(T['left']):
    yield x

  yield T['value']

  for x in inorder(T['right']):
    yield x

# ( 7 + 8 ) * ( 88 + 99 )
tree = lambda : defaultdict(tree) # use the function object 'tree' if missing vals (creates an empty dict)
T = tree()
T['value'] = '*'

T['left']['value'] = '+'
T['left']['left']['value'] = 7
T['left']['right']['value'] = 8

T['right']['value'] = '+'
T['right']['left']['value'] = 88
T['right']['right']['value'] = 99

postfix = ' '.join(str(x) for x in postorder(T))
print(postfix)
pfix = ' '.join(str(x) for x in postorder2(T))
print(pfix)
preorder = ' '.join(str(x) for x in preorder(T))
print(preorder)
infix = ' '.join(str(x) for x in inorder(T))
print(infix)

# Evaluating the 'algebra' of generators, co-routines, decorators
# boils down to knowing the rules of execution for each
# and knowing when things happen
# Then it is just a matter of applying those rules
# This holds in general for evaluating algorithms!
# If you find it hard to understand an algorithm, it may be too complex
# or you just dont know the rules of execution well (the algebra of execution)

#| postorder(T)
#|     postorder(T['left'])
#|         postorder(T['left'])
#|             postorder(T['left'])
#|                 tree is None so return
#|             postorder(T['right'])
#|                 tree is None so return
#|             yield T['value'] = 7           <----- 1
#|
#|         postorder(T['right'])
#|             postorder(T['left'])
#|                 tree is None so return
#|             postorder(T['right'])
#|                 tree is None so return
#|             yield T['value'] = 8           <----- 2
#|
#|         yield T['value'] = '+'             <----- 3
#|
#| ... then the same repeats for the right branch...
#|
#|     postorder(T['right'])
#|         postorder(T['left'])
#|             postorder(T['left'])
#|                 tree is None so return
#|             postorder(T['right'])
#|                 tree is None so return
#|             yield T['value'] = 88          <----- 4
#|
#|         postorder(T['right'])
#|             postorder(T['left'])
#|                 tree is None so return
#|             postorder(T['right'])
#|                 tree is None so return
#|             yield T['value'] = 99          <----- 5
#|
#|         yield T['value'] = '+'             <----- 6
#|
#| ... the finally the value for the top level T ...
#V    yield['value'] = '*'                    <----- 7
#V
# ... so next has to be called 7 times at the top level ...

# Multi-Radix numbers

# 4 kinds of approaches:

# 1) property (arithmetic) of strcutures
# 2) recursive solution
# 3) iterative
# 4) coroutine

# goal is to produce the set of multi-radx numbers in lexicographic order given a multi-radix base M
# equivalently, given a list of M positive numbers, produce all lists 'a' of the same length as M
# such that 0 <= a[i] < M[i]

# so if M = [3, 2, 4]
# the total number of lists we could generate would be 3 * 2 * 4 = 24

# we can succinctly describe this in python like so:
from itertools import product
def multiradix_product(M):
  return product(*(range(x) for x in M))

