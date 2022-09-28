#!/usr/bin/env python
from setuptools import setup

VERSION = '0.1.0'

setup(
    name='make-icons',
    version=VERSION,
    py_modules=[
        'make_icons',
    ],
    description='A tool for macOS which generates app icons from a single PNG',
    author='Ilya Novozhilov',
    author_email='illiandro@gmail.com',
    entry_points={
        'console_scripts': [
            'make-icons = make_icons:main',
        ]
    }
)
