from pyhance import (
  string,
  list_,
  dictionary
)

def bytes_to(datatype, encoding=None):
    dtypes = (string, str, list, list_, dict, dictionary, tuple, int)
    
    if datatype not in dtypes:
        raise ValueError(f"data type passed ({datatype}) not in available data types\n{dtypes}")
