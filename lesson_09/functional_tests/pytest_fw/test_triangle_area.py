from lesson_09.test_functions import triangle_area


def test_triangle_area_positive():
    assert triangle_area(1, 1, 1) == 10