# lambdas are anonymous functions
def add(x, y):
  return x + y

add(1, 2)

del add  # rm function def from enviornment

try:
  add(1, 2)
except:
  print("add not defined")

add = lambda x,y: x + y
add(5,6)


# useful for callbacks
# callbacks are functions that will run and notifies
# the caller when it is done, the caller usually goes on to do 
# something else

noargs = lambda : print("function!") # lambdas can have no args
# python 3 allows print 
# python 2 doesn't 
# for + while are not allowed
noargs()

# fors = lambda : for times in range(10): print(times)

# Predicate - function that returns T or F
# lambdas are useful for implementing predicates

is_lambda = lambda x : type(x) == type(lambda : [])
print(is_lambda(noargs))  # True

# lambdas must have expressions
# this doesn't work
# the lambda that does nothing...
# does_nothing = lambda : 

# lambdas can take lambdas
closre = lambda f, args: f(*args)
print(closre(add, (1,2)))

# note the function expansion with *

# lambdas are also good for not polluting namespace
