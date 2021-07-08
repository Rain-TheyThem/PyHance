from math import sqrt


def haversine(point1, point2, sigfigs=2):
    hdist = (point2[0] - point1[0])**2
    vdist = (point2[1] - point1[1])**2
    distance = sqrt(hdist + vdist)
    if type(distance) == float:
        distance = sqrt(hdist + vdist)
    if sigfigs == None:
        return distance
    return round(distance, sigfigs)