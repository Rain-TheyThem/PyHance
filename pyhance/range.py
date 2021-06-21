def range_(stop, start=0, step=1, inclusive=False):
    if inclusive:
        if start > stop:
            return range(start, stop - 1, step)
        return range(start, stop + 1, step)
    elif not inclusive:
        return range(start, stop, step)