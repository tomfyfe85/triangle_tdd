from triangles import triangle_type_machine
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

