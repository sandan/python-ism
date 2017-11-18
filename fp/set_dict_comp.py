# sets are unordered and contains no duplicates
# { expr for x in itr1 if pred1 }
print({x + 1 for x in range(20) if x > 10})

# dicts
# { kexpr: vexpr for (k,v) in itr1 if pred1 }
print({"number: " + str(x): x  for x in range(20) if x > 10})
