#!/usr/bin/env python2.7
import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pydidit",
    version="0.0.1",
    author="Valentine Gogichashvili",
    author_email="valgog@gmail.com",
    description=("A simple command line script to publish to iDoneThis"),
    license="BSD",
    keywords="todo idonethis",
    url="http://www.github.com/valgog/pydidit",
    py_modules=['pydidit'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Productivity",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        'Click',
        'requests',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        didit=pydidit.cli:cli
    ''',
)
