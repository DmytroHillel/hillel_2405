from lesson_09.test_functions import triangle_area
import pytest


@pytest.mark.negative
def tc_triangle_area_negative_all_0():
    assert round(triangle_area(0, 0, 0), 3) == 0.0


@pytest.mark.negative
def tc_triangle_area_negative_with_none():
    with pytest.raises(TypeError):
        assert round(triangle_area(None, 'a', 's'), 3) == 0.433