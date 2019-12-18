#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import re

package = "periodrangepy"

with open("README.md", "r", encoding="utf8") as fh:
    readme = fh.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


setup(
    name='periodrangepy',
    version=get_version(package),
    description="Генерация списка периодов",
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=['periodrangepy'],
    install_requires=['python-dateutil'],
    license='MIT',
    url='https://github.com/pavelmaksimov/periodrangepy',
    author='Pavel Maksimov',
    keywords="date,period,python,range",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.5',
)
