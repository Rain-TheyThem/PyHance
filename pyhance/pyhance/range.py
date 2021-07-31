def range_(stop, start=0, step=1, inclusive=False):
    """
    A function to return a range of numbers,
    starting at start (which defaults to 0),
    ending at end, and increments each number by step (which defaults to 1), with an option to be inclusive.
    """
    if inclusive:
        if start > stop:
            return range(start, stop - 1, step)
        return range(start, stop + 1, step)
    elif not inclusive:
        return range(start, stop, step)
