# list comprehensions apply an expression over list, tuple, dict, any Iterable
# list comps can be faster than for

# a lambda that evaluates boolean expressions
pred = lambda bool_exp : bool_exp
print(pred(10 > 9))

add_1 = lambda x : x + 1
x1 = [add_1(t) for t in range(20)]
x2 = [add_1(t) for t in range(20) if pred(t > 10)]

print(x1)
print(x2)

pred1 = lambda x: x > 10

# "promise" list comps
lc = lambda expr, itr, pred: [expr(x) for x in itr if pred(x)]
x1 = lc(add_1, range(20), lambda x: True)
x2 = lc(add_1, range(20), pred1)

print(x1)
print(x2)
