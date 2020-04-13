from functools import reduce

from .reducers import reduce_by_boro, reduce_by_species, reduce_species_by_val, reduce_by_nta

class Processor:
  def count_per_boro(data):
    if not data or not isinstance(data, list):
      raise TypeError('Expecting data to be a List')
    return reduce(reduce_by_boro, data, {})

  def count_species(data):
    if not isinstance(data, list):
      raise TypeError('Expecting boro to be a string')
    first_pass = reduce(reduce_by_species, data, {})
    second_pass = reduce_species_by_val(first_pass)
    return second_pass

  def count_per_nta(data):
    if not data or not isinstance(data, list):
      raise TypeError('Expecting data to be a List')
    return reduce(reduce_by_nta, data, {})

