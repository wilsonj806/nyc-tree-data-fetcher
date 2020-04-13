import re

def check_species(species):
  pattern = '(chestnut|ash|cherry|lilac|maple|oak|elm|birch|pine|linden|willow|cedar)'
  return re.findall(pattern, species)

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
  check = check_species(dictname)
  simplify = check[0] if check else dictname
  if not simplify in acc:
    newentry = { simplify: 1 }
    acc.update(newentry)
  else:
    acc[simplify] += 1
  return acc

def reduce_species_by_val(inputdict):
  res = { 'other': 0 }
  for key in inputdict:
    if (inputdict[key] <= 5):
      res['other'] += inputdict[key]
    else:
      newentry = { key: inputdict[key] }
      res.update(newentry)
  return res

def reduce_by_nta(acc, inputdict):
  dictname = inputdict['nta_name']
  if not dictname in acc:
    newentry = { dictname: 1 }
    acc.update(newentry)
  else:
    acc[dictname] += 1
  return acc