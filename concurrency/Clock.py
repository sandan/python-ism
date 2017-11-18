from threading import Thread
from time import ctime, sleep
from logging import DEBUG, debug, basicConfig

basicConfig(level=DEBUG, format="%(threadName)s %(message)s")
class Clock(Thread):

  def __init__(self, interval):
    super().__init__()

    # private attrbutes
    self.__nap = interval
    self.__stop = False

  def cancel(self):
    debug("Clock stopped")
    self.__stop = True

  def run(self):
    debug("Clock started")
    while(True):
      if self.__stop:
        break
      debug(ctime())
      sleep(self.__nap)
