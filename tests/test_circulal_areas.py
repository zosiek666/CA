# -*- coding: utf-8 -*-
import pytest
from circular_areas import CircularAreas

SURFACES = [(42.6, -5.6, 1000, 1), (48.858156, 2.294776, 1000, 2), (48.858284, 2.297882, 100, 3)]
SURFACES_BAD_IDS = [5, 6, 7, 8]
EXTRA_SURFACE = [(51.128542, 16.983429, 1000, 4)]
POINTS = [(42.600107, -5.6, [1]), (42.59997, -5.6, [1]), (44.69, -2.827, []), (48.858243, 2.297972, [3, 2]),
          (48.857507, 2.286091, [2]), (48.853203, 2.274404, [])]
EXTRA_POINTS = POINTS + [(51.128313, 16.985274, [4]), (51.137878, 17.038865, [])]


@pytest.fixture(scope='module')
def CircularAreaObject():  # noqa
    CA = CircularAreas()
    return CA


class TestCircularAres(object):
    def test_add_surfaces(self, CircularAreaObject):
        CircularAreaObject.batch_create(SURFACES)

    @pytest.mark.parametrize('point', POINTS)
    def test_points_are_in_surfaces(self, point, CircularAreaObject):
        assert CircularAreaObject.query(point[0], point[1]) == point[2]

    @pytest.mark.parametrize('surface', SURFACES)
    def test_surface_id_is_proper_with_data(self, surface, CircularAreaObject):
        assert CircularAreaObject.get_area(surface[3]) == {'lat': surface[0], 'long': surface[1], 'radius': surface[2]}

    def test_add_extra_surfaces(self, CircularAreaObject):
        CircularAreaObject.batch_create(EXTRA_SURFACE)

    @pytest.mark.parametrize('point', EXTRA_POINTS)
    def test_with_extra_points_are_in_surfaces(self, point, CircularAreaObject):
        assert CircularAreaObject.query(point[0], point[1]) == point[2]

    @pytest.mark.parametrize('surface', SURFACES)
    def test_with_extra_surface_id_is_proper_with_data(self, surface, CircularAreaObject):
        assert CircularAreaObject.get_area(surface[3]) == {'lat': surface[0], 'long': surface[1], 'radius': surface[2]}

    @pytest.mark.parametrize('surface', SURFACES_BAD_IDS)
    def test_get_not_existing_surface(self, surface, CircularAreaObject):
        assert CircularAreaObject.get_area(surface) == {'error': 'Area dose not exists'}
