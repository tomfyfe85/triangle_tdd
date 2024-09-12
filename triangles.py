import math

"""triangle_type_machine confirms type of triangle from coordinates passed as an argument"""
def triangle_type_machine(coords):
    if  len(coords) < 3 or len(coords) > 3:
        raise Exception("A triangle has must only have 3 coordinates")

    # unpack coords
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    x3, y3 = coords[2]

    side1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    side2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    side3 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

    if side1 != side2 and side2 != side3 and  side3 != side1:
        return "Scalene"


# find length of sides from coordinates
# use to determine isosceles, equilateral

# Equilateral Triangle
# Definition: A triangle in which all three sides are equal in length,
# and all three internal angles are equal, each measuring 60°.

# Isosceles Triangle
# Definition: A triangle in which at least two sides are of equal length,
# and the angles opposite those sides are equal.

# Scalene Triangle
# Definition: A triangle in which all three sides have different lengths,
# and all three internal angles are different.