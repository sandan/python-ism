#!/Users/ms186122/anaconda/bin
# mmap for high perf

# MAP_SHARED = shared memory btw process & threads
# MAP_PRIVATE = available only to proc
# PROT_READ, PROT_WRITE

# close() /flush() will do disk I/O
# close() does an automatic flush()
# call flush() to update disk

import sys,os
from os import O_RDWR
from mmap import mmap, MAP_SHARED, PROT_READ, PROT_WRITE

file = sys.argv[1]
flen = os.path.getsize(file)
fd = os.open(file, O_RDWR)

buf = mmap(fd, flen, MAP_SHARED, PROT_READ|PROT_WRITE)
# the write is needed since flush() is called and written to disk
# if MAP_PRIVATE the file wont be flush() ed to the disk

print(buf[:])

# you can use python slicing to operate on the mmap'd buffer
buf[:] = buf[:].lower()  # in-memory uppercase!
buf.close()
os.close(fd)

# this will change the file in disk too because of the buf.close()
