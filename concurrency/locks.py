# Lock is a mutex
# locks block by default
# acquire() and release() call the lock
# with statement given a lock will call acquire and release

from threading import Lock, Semaphore, Thread, current_thread, enumerate
from time import sleep
from logging import debug, basicConfig, DEBUG
basicConfig(level=DEBUG, format="%(threadName)s %(message)s")

class Counter(object):

  def __init__(self, start = 0):
    self.__lock = Lock()
    self.__value = start

  # two versions of increment
  def inc(self):
    with self.__lock:
      debug("Acquired lock")
      self._value += 1
    debug("Released lock")

  def incr1(self):
    self.__lock.acquire()
    try:
      debug("Acquired lock")
      self._value += 1
    finally:
      self.__lock.release()
      debug("Released lock")

# semaphores
# counter based lock
# acquire() -1 (downs)
# release() +1 (up)
# zero semaphore makes acquire() block

# there is also a BoundedSemaphore class
# raises a ValueError if counts are different (release(), acquire())

# Pool of threads (the list should containt thread objects)
class ThreadPool(object):

  def __init__(self):
    self.__active = [] # the pool
    self.__lock = Lock()

  def makeActive(self, t):   # add to pool
    with self.__lock:  # is this needed? list methods are atomic?
      self.__active.append(t)
      debug("Add: %s", self.__active)

  def makeInactive(self, t): # remove from pool
    with self.__lock:
      self.__active.remove(t)
      debug("Removed: %s", self.__active)

def myThread(sem, pool):
  debug("Waiting to join pool...")
  with sem:
    # critical section
    pool.makeActive(current_thread())
    sleep(3)
    pool.makeInactive(current_thread())

# re-entrant locking
# locks that can be acquired more than once by the same thread
# thread owning the lock can nest acquire() and release()

#    A reentrant lock must be released by the thread that acquired it. Once a
#    thread has acquired a reentrant lock, the same thread may acquire it again
#    without blocking; the thread must release it once for each time it has
#    acquired it.
#    useful for nested aqcuire()s and release()s

from threading import RLock

# if you use a Lock(), program will hang bc it deadlocked itself when calling addBoth
def pair(P):
  pause = 2
  sleep(pause)
  P.addLeft(1)
  P.addRight(-1)
  P.addBoth(1)

class Pair():
  def __init__(self, left=0, right=0):
    self.__left = left
    self.__right = right
    self.__lock = RLock()

  def addLeft(self, val):
    with self.__lock:
      debug("Add to left by %d" % val)
      self.__left += val

  def addRight(self, val):
    with self.__lock:
      debug("Add to right by %d" % val)
      self.__right += val

  def addBoth(self, val):
    with self.__lock:
      debug("Add to pair by %d" % val)
      self.addLeft(val)
      self.addRight(val)

  def __str__(self):
    return "%d %d" % (self._left, self._right)

# thread events
# Event() used to communicate betwen threads
# One thread signals an event while other threads wait

# one thread does something
# another thread does another thing
# we want them to run in the background
# and take an action when they're both done
# want two different threads to take an action on an object at roughly the same time
# - lets two threads notify each other to take action at roughy the same time in the background

# condition variables
# wait()
# notifyAll()
# use acquire() and release() with condition variable (and with)
# Condition object creates its own lock or you can provide it with one

# thread local
# guarantees unique storage for every thread
# visible only to a specific thread
# -python maintains a separate instance dict for each thread
# import local() from threading, local() returns a thread-local storage
# local() can be monkey-patched with attributes
#__enter__() and __exit__() are used for with statements

if __name__ == '__main__':

  pool = ThreadPool()
  sem = Semaphore(3)

  for i in range(4):
    thread = Thread(target=myThread, args=(sem, pool))
    thread.start()

#    main_thread = current_thread()
#    for t in enumerate():
#      if t is not main_thread:
#        t.join()
#
  sleep(30)

  debug("sleeping...")
  p = Pair(0,0)
  for i in range(4):
    thread = Thread(target=pair, args=(p,))
    thread.start()

  sleep(30)
  debug("done")


