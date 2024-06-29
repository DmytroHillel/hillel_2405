import os

from lesson_09.test_functions import triangle_area
import pytest


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.xfail(reason='jira issue 1')
def tc_triangle_area_positive_x_fail():
    assert round(triangle_area(0, 10, 10), 3) == 100


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.xfail(reason='jira issue 2, some description')
def tc_triangle_area_positive_x_pass():
    pass
    # assert round(triangle_area(0, 10, 10), 3) == 100


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.skip(reason='jira issue 3, some description')
def tc_triangle_area_positive_skip():
    assert round(triangle_area(0, 10, 10), 3) == 100


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.skipif(os.getenv('CUR_DB', None) != 'POSTGRES', reason='Only for Postgres')
def tc_triangle_area_positive_skip_if():
    assert round(triangle_area(0, 10, 10), 3) == 100


@pytest.mark.smoke
@pytest.mark.positive
def tc_triangle_area_positive_skip_inside():
    pytest.skip("Only for dev")
    # assert round(triangle_area(0, 10, 10), 3) == 100