#!/usr/bin/env python
from setuptools import find_packages, setup

setup(name='celery-singleton',
      version='0.4.2',
      description='Extend opensource version with pickle support',
      url='https://github.com/SakornW/celery-singleton',
      packages=find_packages(exclude=('tests', 'sample',)),
      install_requires=['celery>=4',
                        'redis'],
      python_requires='>=3.6,<4.0')


# NOTE:
# python setup.py sdist bdist_wheel
# twine upload --repository acommerce dist/*
#
