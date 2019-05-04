from __future__ import absolute_import
from setuptools import setup


setup(
    name="symmath",
    version="0.3",
    packages=["symmath"],
    install_requires=[
        'lxml==3.8.0',
        'six',
        "sympy",
    ],
    test_suite='symmath.tests',
    tests_require=[
        'coverage',
    ],
)
