# application
import sys
from time import sleep
from Clock import Clock


if len(sys.argv) < 2:
  raise SystemExit("Usage: %s interval" % sys.argv[0])

interval = float(sys.argv[1])
def doSomething(): sleep (5*interval)

try:
  clock = Clock(interval)
  clock.start() # note that thread.daemon is False
  doSomething()
except KeyboardInterrupt:
  sys.exit(1)
finally:
  clock.cancel()
