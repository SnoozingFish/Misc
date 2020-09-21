import math

# Unit vectors in axis directions.
vector_i = [1, 0, 0]
vector_j = [0, 1, 0]
vector_k = [0, 0, 1]

#-------------------------------------------------------------------------------
def magnitude(vector):
    """Calculates the magnitude of a vector from its components."""

    rolling_sum = 0
    for i in range(0, len(vector)):
        rolling_sum += vector[i]**2

    return math.sqrt(rolling_sum)
#-------------------------------------------------------------------------------
def scalar_mult(vector, scalar):
    """Multiplies a vector by a scalar."""

    return [i * scalar for i in vector]
#-------------------------------------------------------------------------------
def make_unit_v(vector):
    """Converts a vector to a unit vector in the same direction."""

    return scalar_mult(vector, (1 / magnitude(vector)))
#-------------------------------------------------------------------------------
def dot_prod(vector1, vector2):
    """Calculates the dot product of two vectors."""

    if len(vector1) != len(vector2):
        return None

    dot_prod = 0
    for i in range(0, len(vector1)):
        dot_prod += vector1[i] * vector2[i]

    return dot_prod
#-------------------------------------------------------------------------------
def cross_prod(vector1, vector2):
     """Calculate the cross product of two vectors"""
     # Note: I'm hardcoding the determinants even though I'm sure there's code for that somewhere.

     i_comp = vector1[1] * vector2[2] - vector2[1] * vector1[2]
     j_comp = vector1[0] * vector2[2] - vector2[0] * vector1[2]
     k_comp = vector1[0] * vector2[1] - vector2[0] * vector1[1]

     return [i_comp, -1 * j_comp, k_comp]
#-------------------------------------------------------------------------------
def is_parallel(vector1, vector2):
    """Returns true if vector1 and vector2 are parallel."""

    if dot_prod(vector1, vector2) == magnitude(vector1) * magnitude(vector2):
        return True
    else:
        return False
#-------------------------------------------------------------------------------
def is_perpendicular(vector1, vector2):
    """Returns true if vector1 and vector2 are perpendicular."""

    if dot_prod(vector1, vector2) == 0:
        return True
    else:
        return False
#-------------------------------------------------------------------------------
def angle_between(vector1, vector2):
    """Calculates the angle theta between two vectors"""

    radians = math.acos(dot_prod(vector1, vector2) / (magnitude(vector1) * magnitude(vector2)))
    return "Radians: {} \nDegrees: {}".format(radians, radians * 180 / math.pi)
#-------------------------------------------------------------------------------

a = [3,4,5]
b = [5,4,3]
c = [1,1,1]

p1p2 = [10.333,-8.857,-33.951]

print(scalar_mult(p1p2, -7/10.333))
