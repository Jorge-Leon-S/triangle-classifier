import math
from triangle import classify_triangle, is_valid_triangle
def test_valid_triangle():
    assert is_valid_triangle(3, 4, 5) is True
    assert is_valid_triangle(5, 5, 5) is True
    assert is_valid_triangle(5, 4, 7) is True
def test_non_positive_side_is_invalid():
    assert classify_triangle(0, 4, 5) == "Invalid"
    assert classify_triangle(-1, 4, 5) == "Invalid"
def test_degenerate_triangle_is_invalid():
    assert is_valid_triangle(1, 2, 3) is False
    assert classify_triangle(1, 2, 3) == "Invalid"
def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"
    assert classify_triangle(5, 5, 5) == "Equilateral"
def test_isosceles_triangle():
    assert classify_triangle(5, 5, 6) == "Isosceles"
    assert classify_triangle(5, 6, 5) == "Isosceles"
    assert classify_triangle(6, 5, 5) == "Isosceles"
def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"
    assert classify_triangle(5, 6, 4) == "Scalene"
    assert classify_triangle(6, 4, 5) == "Scalene"
def test_right_triangle_with_non_integer_side():
    assert classify_triangle(1, 1, math.sqrt(2)) == "Right Isosceles"
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"
def test_equilateral_triangle_is_not_right():
    assert classify_triangle(1, 1, 1) == "Equilateral"
    assert classify_triangle(5, 5, 5) == "Equilateral"
def test_triangle_inequality_is_violated():
    assert is_valid_triangle(1, 2, 4) is False
    assert classify_triangle(1, 2, 4) == "Invalid"