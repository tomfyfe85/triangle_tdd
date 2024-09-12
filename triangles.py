"""triangle_type_machine confirms type of triangle from coordinates passed as an argument"""

def triangle_type_machine(coordinates):
    if  len(coordinates) < 3 or len(coordinates) > 3:
        raise Exception("A triangle has must only have 3 coordinates")




# find length of sides from coordinates
# use to determine isosceles, equilateral

# 1. Equilateral Triangle
# Definition: A triangle in which all three sides are equal in length,
# and all three internal angles are equal, each measuring 60°.

# 2. Isosceles Triangle
# Definition: A triangle in which at least two sides are of equal length,
# and the angles opposite those sides are equal.

# 3. Scalene Triangle
# Definition: A triangle in which all three sides have different lengths,
# and all three internal angles are different.