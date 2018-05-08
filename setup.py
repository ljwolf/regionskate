#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'regionskate'
DESCRIPTION = 'A fast sparse algorithm for spatial regionalization.'
URL = 'https://github.com/ljwolf/regionskate'
EMAIL = 'levi.john.wolf@gmail.com'
AUTHOR = 'Levi John Wolf'

# What packages are required for this module to be executed?
required = ['numpy','scipy','scikit-learn','region'
    # 'requests', 'maya', 'records',
]

# Dependencies only for versions less than Python 2.7:
# if sys.version_info < (2, 7):
#     required.append('requests[security]')

# Where the magic happens:
setup(
    name=NAME,
    version="1.0.1",
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    install_requires=['region'],
    include_package_data=True,
    license='ISC',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
