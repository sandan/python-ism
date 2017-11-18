import sys
from threading import Thread
from time import sleep, ctime
from logging import basicConfig, debug, ERROR, DEBUG
basicConfig(level=DEBUG, format="%(threadName)s %(message)s",)

if len(sys.argv) < 2:
  raise SystemExit("Usage...")

interval = float(sys.argv[1])
doSomething = lambda : sleep(5*interval)

def myClock(nap):
    debug("clock started...")
    while (True):
      print(ctime())
      sleep(nap)

try:
  clock = Thread(target=myClock, args=(interval,))
  clock.daemon = True   # set before start()ing thread
                        # when main thread terminates
                        # the daemon thread terminates
                        # if False, daemon Thread continues to live on
                        # set this to False to see, stop with ctrl + z
                        # the python program lives on still even though main exits
  clock.start()
  doSomething()  # main thread calls

except KeyboardInterrupt:
  sys.exit(1)
finally:
  debug("stopped")

