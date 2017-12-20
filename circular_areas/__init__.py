# -*- coding: utf-8 -*-
import os
from .circular_areas import CircularAreas

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

VERSION = (1, 0, 0)  # PEP 386
__version__ = ".".join([str(x) for x in VERSION])
__all__ = ['CircularAreas']
