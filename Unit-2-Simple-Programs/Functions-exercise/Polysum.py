import math

def polysum(n, s):
    """
    n: number of sides of regular polygon
    s: length of the side

    returns: the sum of the area and the square of the perimeter
             (rounded to 4 decimal places)
    """

    area = (0.25 * n * s ** 2) / (math.tan(math.pi / n))
    perimeter = n * s
    result = area + perimeter ** 2
    
    return round(result, 4)


print(polysum(3, 100))

    
