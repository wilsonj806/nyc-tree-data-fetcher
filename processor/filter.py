# (boro) => (row) => return Boolean if match
def filter_by_boro(boro):
  return lambda row: True if (row['boroname'] == boro) else False