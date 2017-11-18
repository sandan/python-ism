from threading import Thread, current_thread, enumerate

from random import randint
from time import sleep
from logging import basicConfig, debug, ERROR, DEBUG

basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

# each thread calls this fn
def myThread():
  pause = randint(1, 5)
  debug("sleeping %s" % pause)
  sleep(pause)
  debug("wake up")

if __name__ == '__main__':

  print("main")

  # start 3 threads
  for i in range(3):
    tr = Thread(target=myThread)
    tr.start()  # enqueue

  # joining boilerplate to wait for all threads
  mainThread = current_thread()
  for thread in enumerate():      # 4 threads being enumerated
    if thread is not mainThread:  # can't call join on current_thread()
      debug(" joining %s" % thread.name)
      thread.join()
  #
debug("done")
