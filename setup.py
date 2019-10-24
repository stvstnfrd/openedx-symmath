from __future__ import absolute_import
from setuptools import setup


setup(
    name="symmath",
    version="0.4",
    packages=["symmath"],
    install_requires=[
        'lxml',
        'six',
        "sympy",
    ],
    test_suite='symmath.tests',
    tests_require=[
        'coverage',
    ],
)
