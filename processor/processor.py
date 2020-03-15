from functools import reduce

def reduce_by_boro(acc, inputdict):
  dictname = inputdict['boroname']
  if not inputdict['boroname'] in acc:
    newentry = { dictname: 1}
    acc.update(newentry)
  else:
    acc[dictname] += 1
  return acc

class Processor:
  def return_per_boro(data):
    if not data or not isinstance(data, list):
      raise TypeError('You used it wrong')
    return reduce(reduce_by_boro, data, {})


