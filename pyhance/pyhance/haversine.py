from math import sqrt


def haversine(point1, point2, sigfigs=2):
    """
    A standalone function to find the distance between two points, passed as tuples.

    Parameters
    ----------
    point1: the first tuple of coordinates
    point2: the second tuple of coordinates
    sigfigs: the number of decimal places to return. Pass None to return all sigfigs.
    """
    hdist = (point2[0] - point1[0])**2
    vdist = (point2[1] - point1[1])**2
    distance = sqrt(hdist + vdist)
    if type(distance) == float:
        distance = sqrt(hdist + vdist)
    if sigfigs == None:
        return distance
    return round(distance, sigfigs)
