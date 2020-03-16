from functools import reduce

def reduce_by_boro(acc, inputdict):
  dictname = inputdict['boroname']
  if not inputdict['boroname'] in acc:
    newentry = { dictname: 1}
    acc.update(newentry)
  else:
    acc[dictname] += 1
  return acc

def reduce_by_species(acc, inputdict):
  # IF the current entry is a Stump
  if inputdict['status'] == 'Stump' and not 'stump' in acc:
    newentry = { 'stump': 1 }
    acc.update(newentry)
    return acc
  elif inputdict['status'] == 'Stump':
    acc['stump'] += 1
    return acc

  # IF the current entry is Dead
  if inputdict['status'] == 'Dead' and not 'dead' in acc:
    newentry = { 'dead': 1 }
    acc.update(newentry)
    return acc
  elif inputdict['status'] == 'Dead':
    acc['dead'] += 1
    return acc

  # ELSE check if the tree exists
  dictname = inputdict['spc_common']
  if not dictname in acc:
    newentry = { dictname: 1 }
    acc.update(newentry)
  else:
    acc[dictname] += 1
  return acc

class Processor:
  def count_per_boro(data):
    if not data or not isinstance(data, list):
      raise TypeError('Expecting data to be a List')
    return reduce(reduce_by_boro, data, {})

  def count_species(data):
    print('dookie')
    if not isinstance(data, list):
      raise TypeError('Expecting boro to be a string')
    return reduce(reduce_by_species, data, {})

