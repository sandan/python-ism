from functools import wraps

def select(columns=None, **kw):
  def decorate(fn):
    @wraps(fn)
    # error/logging for select
    def inner(*args, **kwargs):
      # arg-preprocessing for fn
      res =  fn(*args, **kwargs)
      # arg-postprocessing for fn
      return res
    return inner
  return decorate

def from(sources=None, **kw):
  def decorate(fn):
    @wraps(fn)
    # error/logginf for from
    def inner(*args, **kwargs):
      # arg-preprocesing for fn
      res = fn(*args, **kwargs)
      # arg post-processing for fn
      return res
    return inner
  return decorate

@select(columns = ["c1", "c2"])
@from(table = ["t1"])
def build_sql(*args, **kw):
  res = None
  for i in args:
    res = res + i  # reduce
  res = res + ";"
  return res
