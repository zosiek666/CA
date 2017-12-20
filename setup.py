# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

###########################
NAME = 'circular_areas'
assert NAME
###########################


def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(os.path.join(os.getcwd(), *f)).readlines()]))  # noqa


init = os.path.join(os.path.dirname(__file__), NAME, '__init__.py')
version_line = list(filter(lambda l: l.startswith('VERSION'), open(init)))[0]
VERSION = get_version(eval(version_line.split('=')[-1]))
assert VERSION

PACKAGES = find_packages(exclude=['samples', 'tests'])
PACKAGE_DIR = {'': '.'}
LONG_DESCRIPTION = open("README.md").read()
INSTALL_REQUIRES = reqs('requirements.txt')
TESTS_REQUIRES = reqs('tests_requirements.txt')

setup(name=NAME,
      version=VERSION,
      author='Karol Narowski',
      author_email='karol@narowski.com.pl',
      url='http://narowski.com.pl/',
      package_dir=PACKAGE_DIR,
      packages=PACKAGES,
      test_suite='py.test',
      zip_safe=False,
      install_requires=INSTALL_REQUIRES,
      tests_require=TESTS_REQUIRES,
      long_description=LONG_DESCRIPTION)  # noqs
