#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os
import sys

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'regionskate'
DESCRIPTION = 'A fast sparse algorithm for spatial regionalization.'
URL = 'https://github.com/ljwolf/regionskate'
EMAIL = 'levi.john.wolf@gmail.com'
AUTHOR = 'Levi John Wolf'

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary. 
about = {}
with open(os.path.join(here, NAME, "__version__.py")) as f:
    exec(f.read(), about)

# Support "$ setup.py publish".
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()

# What packages are required for this module to be executed?
required = ['numpy','scipy','scikit-learn','pysal'
    # 'requests', 'maya', 'records',
]

# Dependencies only for versions less than Python 2.7:
# if sys.version_info < (2, 7):
#     required.append('requests[security]')

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
#     entry_points={
#         'console_scripts': ['mycli=mymodule:cli'],
#     },
    install_requires=required,
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
