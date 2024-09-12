from triangles import triangle_type_machine
import math
import pytest

def test_error_with_less_than_three_coords():
    """Exception raised if there are less than 3 coordinates"""
    with pytest.raises(Exception) as e:
        triangle_type_machine([(0, 0), (0, 1)])
    error_msg = str(e.value)
    assert error_msg == "A triangle has must only have 3 coordinates"

def test_error_with_more_than_three_coords():
    """Exception raised if there are more than 3 coordinates"""
    with pytest.raises(Exception) as e:
        triangle_type_machine([(0, 0), (0, 1), (0, 0), (0, 1)])
    error_msg = str(e.value)
    assert error_msg == "A triangle has must only have 3 coordinates"

def test_is_a_scalene_triangle():
    assert triangle_type_machine([(0,0), (3,4), (6,6)]) == "Scalene"

def test_is_an_isosceles_triangle():
    assert triangle_type_machine([(1,2), (5,2), (3,6)]) == "Isosceles"


# TODO
# find coords for a triangle with 3 internal angles of 60 degrees
# last coord of c must be square root
# def test_is_an_equilateral_triangle():
#     assert triangle_type_machine([(0, 0), (2, 0), (1, math.sqrt(3))]) == "Equilateral"