def rint(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False


def rstr(obj):
    try:
        str(obj)
        return True
    except ValueError:
        return False


def rlist(obj):
    if (
        len([char for char in obj if char == "["])
        and len([char for char in obj if char == "]"])
    ) > 0:
        return True
    return False


def rtuple(obj):
    if (
        len([char for char in obj if char == "("])
        and len([char for char in obj if char == ")"])
    ) > 0:
        return True
    return False


def rdict(obj):
    if (
        len([char for char in obj if char == "{"])
        and len([char for char in obj if char == "}"])
    ) > 0:
        return True
    return False


def rfloat(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False