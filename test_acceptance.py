from triangle import classify_triangle

def test_stained_glass_customer_requirements():
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(0, 4, 5) == "Invalid"
    assert classify_triangle(5, 5, 5) == "Equilateral"
    assert classify_triangle(5, 5, 6) == "Isosceles"
    assert classify_triangle(4, 5, 6) == "Scalene"
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 5, 5 * 2**0.5) == "Right Isosceles"