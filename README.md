
# Triangle Classifier

## Overview

This Python project validates three side lengths and classifies
valid triangles as Equilateral, Isosceles, or Scalene.
Right triangles receive a "Right" prefix.

Invalid triangles return "Invalid".

## Requirements

- Python 3.10 or newer
- pytest

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the tests

Run all unit and acceptance tests:

```bash
python -m pytest -v
```

Run only the unit tests:

```bash
python -m pytest -v test_triangle.py
```

Run only the acceptance test:

```bash
python -m pytest -v test_acceptance.py
```

## Equivalence Classes and Boundaries

| Class or boundary | Example | Expected result |
|---|---|---|
| Zero side | (0, 4, 5) | Invalid |
| Negative side | (-1, 4, 5) | Invalid |
| Degenerate boundary | (1, 2, 3) | Invalid |
| Violates triangle inequality | (1, 2, 4) | Invalid |
| All sides equal | (5, 5, 5) | Equilateral |
| Exactly two sides equal | (5, 5, 6) | Isosceles |
| All sides different | (4, 5, 6) | Scalene |
| Integer right triangle | (3, 4, 5) | Right Scalene |
| Non-integer right triangle | (5, 5, 5*sqrt(2)) | Right Isosceles |

The triangle inequality requires the sum of any two sides to be
strictly greater than the third side. Equality is invalid.

## Why an Equilateral Triangle Cannot Be Right

In an equilateral triangle, all three angles are 60 degrees.
A right triangle must have one angle equal to 90 degrees.
Therefore, an equilateral triangle cannot be a right triangle.

## Copilot Review Log

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
|---|---|---|---|
| test_isosceles_triangle | Yes | Kept | examples have exactly two equal sides. Testing different side positions is useful because it checks that your code doesn't depend on the order of the arguments. |
| test_right_triangle_with_non_integer_side | Yes | Edited | Despite the test's name, most examples have integer sides. |
| test_triangle_inequality_is_violated | No | Added | Covers an invalid triangle that violates the inequality without being degenerate. |

## Acceptance Criteria

1. Any nonpositive side or failed triangle inequality returns
   "Invalid" without raising an exception during classification.
2. Valid triangles return the correct ordinary shape classification.
3. Valid right triangles return a classification beginning with
   "Right ", so they can be identified for reinforced corners.

## AI-Use Disclosure

Tool: GitHub Copilot.

Used for: Drafting unit-test suggestions and reviewing possible
test cases for the triangle classifier.

What I verified: I compared suggestions against the assignment
specification, checked the degenerate boundary, reviewed the
floating-point tolerance requirement, and ran the tests.