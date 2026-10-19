import math
def is_valid_triangle(a, b, c) -> bool:
    """Returns True if three side lengths form a triangle"""
    if a <=0 or b<=0 or c<=0:
        return False
    return (
        a + b > c
        and a + b + c
        and b + c > a
    )

def classify_triangle(a, b, c,) -> str:
    """Classify a triangle and prefix its type if it is right angled."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isoceles"
    else:
        triangle_type = "Scalene"
    x, y, z, = sorted((a,b,c))
    if math.isclose(
        x*x+y*y,
        x*z,
        rel_tol=1e-9,
        abs_tol=1e-9,
    ):
        return f"Right {triangle_type}"
    return triangle_type