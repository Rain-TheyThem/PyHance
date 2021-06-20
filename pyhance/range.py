def range_(stop, start=0, step=1, inclusive=False):
    if inclusive:
        i = start
        nums = []
        while i <= stop:
            nums.append(i)
            i += step
        return nums
    elif not inclusive:
        i = start
        nums = []
        while i < stop:
            nums.append(i)
            i += step
        return nums
