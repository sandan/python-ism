# persist a dict to disk
# keys should strings
# works with nested objects
# serializes and deserializes objects to dbm files
# 

import shelve

d = {"a": 1, "b": 2, "next": {"c": 3, "d": 4 }}
print(d)
sdb = shelve.open("d") # open or create file

#sdb is a shelf object
print(type(sdb))

# you can treat sdb like a dict
for k, v in d.items():
  print("adding:  ",k ,v)
  sdb[k] = v  # has a __getitem__

sdb.close()  # like mem-mapping, flushes dict to disk

# read from dbm to dict in memory
nsdb = shelve.open("d", "r") # if you dont give the 'r' it is open for write
print("read data loaded from file")
for k, v in nsdb.items():
  print(k,v)

nsdb.close()

# update to the shelf
wsdb = shelve.open("d", writeback=True) # f you dont use writeback, file wont get updated
wsdb['next']['next'] = {"e": 5, "f": 6, "g": 7}

wsdb.close()

# read updated dict
nsdb = shelve.open("d", "r") # if you dont give the 'r' it is open for write
print("read data loaded from file")
print("reading updated dict:")
for k, v in nsdb.items():
  print(k,v)

nsdb.close()
