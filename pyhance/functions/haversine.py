def haversine(point1, point2, sigfigs=2):

    """
    The haversine function takes two Point objects or two tuples*
    of X and Y coordinates, and calculates the distance.


    Arguments
    
    point1: the first point object or tuple*
    point2: the second point object or tuple*
    sigfigs: the number of figures after the decimal place.
    If a number, will round (5+ rounds up, 4- rounds down)
    to the specified number.
    If None, will not round,
    and will return all numbers after the decimal place,
    with no padding 0s.

    * The contents of the tuples must be: (X, Y)


    Return

    Returns the shortest distance between the two points,
    with the number of signifigant figures specicifed in 
    the sigfigs argument.


    Type

    Returns a float that is the distance between the two points.
    point1 and point2 may be either tuples or Point objects
    (see documentation).
    """

    from math import sqrt
    hdist = (point2[0] - point1[0])**2
    vdist = (point2[1] - point1[1])**2
    distance = sqrt(hdist + vdist)
    if type(distance) == float:
        distance = sqrt(hdist + vdist)
    if sigfigs == None:
        return distance
    return round(distance, sigfigs)