# -*- coding: utf-8 -*-
import pytest
from circular_areas import CircularAreas

SURFACES = [(42.6, -5.6, 1000, 1), (48.858156, 2.294776, 1000, 2)]
POINTS = [[(42.600107, -5.6), [1]], [(42.59997, -5.6), [1]],
          [(48.858243, 2.297972), [2]], [(48.857507, 2.286091), [2]],
          [(44.69, -2.827), []], [(48.853203, 2.274404), []]]
EXTRA_SURFACES = [(22.6, -25.6, 1000, 3), (-48.858156, 12.294776, 1000, 4)]
EXTRA_POINTS = [[(22.599001, -25.5915), [3]], [(-48.85, 12.3), [4]]]


@pytest.fixture()
def ca_object():
    ca = CircularAreas()
    ca.batch_create(SURFACES)
    return ca


class TestCircularAreas:

    def test_add_surfaces(self):
        ca = CircularAreas()
        ca.batch_create(SURFACES)
        assert len(ca.areas) == 2

    @pytest.mark.parametrize("point,expected", POINTS)
    def test_points_are_in_surfaces(self, ca_object, point, expected):
        surface_id = ca_object.query(point[0], point[1])
        assert surface_id == expected

    @pytest.mark.parametrize("surface", SURFACES)
    def test_surface_id_is_proper_with_data(self, ca_object, surface):
        actual_surface = ca_object.get_area(surface[3])
        expected_surface = {'lat': surface[0], 'long': surface[1], 'radius': surface[2]}
        assert actual_surface == expected_surface

    def test_add_extra_surfaces(self, ca_object):
        ca_object.batch_create(EXTRA_SURFACES)
        assert len(ca_object.areas) == 4

    @pytest.mark.parametrize("extra_point,expected_id", EXTRA_POINTS)
    def test_with_extra_points_are_in_surfaces(self, ca_object, extra_point, expected_id):
        ca_object.batch_create(EXTRA_SURFACES)
        surface_id = ca_object.query(extra_point[0], extra_point[1])
        assert surface_id == expected_id

    @pytest.mark.parametrize("extra_surface", EXTRA_SURFACES)
    def test_with_extra_surface_id_is_proper_with_data(self, ca_object, extra_surface):
        ca_object.batch_create(EXTRA_SURFACES)
        actual_surface = ca_object.get_area(extra_surface[3])
        expected_surface = {'lat': extra_surface[0], 'long': extra_surface[1], 'radius': extra_surface[2]}
        assert actual_surface == expected_surface

    def test_get_not_existing_surface(self, ca_object):
        assert ca_object.get_area(3) == {'error': 'Area dose not exists'}
