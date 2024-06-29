import os

from lesson_09.test_functions import triangle_area
import pytest


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.class_test
class TestTrianglePositive:

    @pytest.mark.xfail(reason='jira issue 1')
    def tc_class_triangle_area_positive_x_fail(self):
        assert round(triangle_area(0, 10, 10), 3) == 100

    @pytest.mark.xfail(reason='jira issue 2, some description')
    def tc_class_triangle_area_positive_x_pass(self):
        pass
    # assert round(triangle_area(0, 10, 10), 3) == 100

    @pytest.mark.skip(reason='jira issue 3, some description')
    def tc_class_triangle_area_positive_skip(self):
        assert round(triangle_area(0, 10, 10), 3) == 100

    @pytest.mark.skipif(os.getenv('CUR_DB', None) != 'POSTGRES', reason='Only for Postgres')
    def tc_class_triangle_area_positive_skip_if(self):
        assert round(triangle_area(0, 10, 10), 3) == 100
