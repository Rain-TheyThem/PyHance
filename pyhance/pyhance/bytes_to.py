from pyhance.string import string
from pyhance.list import list_
from pyhance.dict import dictionary


def bytes_to(bytes_to_convert, datatype, method="little", byte_number=1):
    """
    Convert a bytes object to the given data type.
    """
    dtypes = (string, str, int)

    if datatype not in dtypes:
        raise ValueError(
            f"data type passed ({datatype}) not in available data types\n{dtypes}"
        )
    else:
        if datatype == string:
            return string(map(chr, bytes))
        elif datatype == str:
            return str(map(chr, bytes))
        elif datatype == int:
            if method in ("little", "big"):
                if type(byte_number) == int:
                    return int.from_bytes(method(byte_number), method)
                else:
                    raise TypeError(
                        f"Invalid data type of byte_number ({byte_number}), type must be int"
                    )
            else:
                raise ValueError(
                    f"Invalid method ({method}), method must be 'big' or 'little'"
                )
