def rint(obj):
    """
    Checks if an object can be converted to an integer
    """
    try:
        int(obj)
        return True
    except ValueError:
        return False


def rstr(obj):
    """
    Checks if an object can be converted to a string
    """
    try:
        str(obj)
        return True
    except ValueError:
        return False


def rlist(obj):
    """
    Checks if there is a list inside of a string (ex. '[1, 2, 3]' would return True)
    """
    if (len([char for char in obj if char == "["])
            and len([char for char in obj if char == "]"])) > 0:
        return True
    return False


def rtuple(obj):
    """
    Checks if there is a tuple inside of a string (ex. '(1, 2, 3)' would return True)
    """
    if (len([char for char in obj if char == "("])
            and len([char for char in obj if char == ")"])) > 0:
        return True
    return False


def rdict(obj):
    """
    Checks if there is a dictionary inside of a string (ex. '{"a": 1, "b": 2, "c": 3}' would return True)
    """
    if (len([char for char in obj if char == "{"])
            and len([char for char in obj if char == "}"])) > 0:
        return True
    return False


def rfloat(obj):
    """
    Checks if an object can be converted to a float
    """
    try:
        int(obj)
        return True
    except ValueError:
        return False
