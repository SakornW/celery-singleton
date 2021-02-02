#!/usr/bin/env python
from setuptools import find_packages, setup

setup(name='celery-singleton',
      version='0.4.3',
      description='Extend opensource version with pickle support',
      url='https://github.com/SakornW/celery-singleton',
      packages=find_packages(exclude=('tests', 'sample',)),
      install_requires=['celery>=4',
                        'redis'],
      python_requires='>=3.6,<4.0')


# NOTE: to build
# delete local build/dist folder.
# python setup.py sdist bdist_wheel
# twine upload --repository acommerce dist/*
#
