# -*- coding: utf-8 -*-
import Geohash
import math
from itertools import chain
from collections import defaultdict


class CircularAreas(object):
    def __init__(self, precision=8):
        self.areas = {}
        self.hashed_areas = {}
        self.precision = precision if precision <= 12 and precision >= 1 else 8

    def get_area(self, id):
        return self.areas.get(id, {'error': 'Area dose not exists'})

    def batch_create(self, areas_list):
        _temp = list(map(lambda x: {x[3]: {'lat': x[0], 'long': x[1], 'radius': x[2]}}, areas_list))
        for _ in _temp:
            self.areas.update(_)
            _id = next(iter(_))
            _geohashes = self._create_geohash(_[_id]['lat'], _[_id]['long'], _[_id]['radius'], self.precision)
            _new_dict = defaultdict(list)
            _dict = dict(zip(_geohashes, [_id] * len(_geohashes)))
            for k, v in chain(_dict.items(), self.hashed_areas.items()):
                if isinstance(v, list):
                    _new_dict[k] = _new_dict[k] + v
                else:
                    _new_dict[k].append(v)
            self.hashed_areas = dict(_new_dict)

    def query(self, lat, long):
        _areas = self.hashed_areas.get(Geohash.encode(lat, long, precision=self.precision), [])
        return _areas

    def _in_circle_check(self, latitude, longitude, centre_lat, centre_lon, radius):
        x_diff = longitude - centre_lon
        y_diff = latitude - centre_lat
        return math.pow(x_diff, 2) + math.pow(y_diff, 2) <= math.pow(radius, 2)

    def _get_centroid(self, latitude, longitude, height, width):
        y_cen = latitude + (height / 2)
        x_cen = longitude + (width / 2)
        return x_cen, y_cen

    def _convert_to_latlon(self, y, x, latitude, longitude):
        r_earth = 6371000
        lat_diff = (y / r_earth) * (180 / math.pi)
        lon_diff = (x / r_earth) * (180 / math.pi) / math.cos(latitude * math.pi / 180)
        final_lat = latitude + lat_diff
        final_lon = longitude + lon_diff
        return final_lat, final_lon

    def _create_geohash(self, latitude, longitude, radius, precision, as_set=True):
        x = 0.0
        y = 0.0
        geohashes = []
        returned = None
        grid_width = [5009400.0, 1252300.0, 156500.0, 39100.0, 4900.0, 1200.0, 152.9, 38.2, 4.8, 1.2, 0.149, 0.0370]
        grid_height = [4992600.0, 624100.0, 156000.0, 19500.0, 4900.0, 609.4, 152.4, 19.0, 4.8, 0.595, 0.149, 0.0199]
        height = (grid_height[precision - 1]) / 2
        width = (grid_width[precision - 1]) / 2
        lat_moves = int(math.ceil(radius / height))
        lon_moves = int(math.ceil(radius / width))
        for i in range(0, lat_moves):
            temp_lat = y + height * i
            for j in range(0, lon_moves):
                temp_lon = x + width * j
                if self._in_circle_check(temp_lat, temp_lon, y, x, radius):
                    x_cen, y_cen = self._get_centroid(temp_lat, temp_lon, height, width)
                    lat, lon = self._convert_to_latlon(y_cen, x_cen, latitude, longitude)
                    geohashes += [Geohash.encode(lat, lon, precision)]
                    lat, lon = self._convert_to_latlon(-y_cen, x_cen, latitude, longitude)
                    geohashes += [Geohash.encode(lat, lon, precision)]
                    lat, lon = self._convert_to_latlon(y_cen, -x_cen, latitude, longitude)
                    geohashes += [Geohash.encode(lat, lon, precision)]
                    lat, lon = self._convert_to_latlon(-y_cen, -x_cen, latitude, longitude)
                    geohashes += [Geohash.encode(lat, lon, precision)]
        returned = set(geohashes) if as_set else ','.join(set(geohashes))
        return returned
