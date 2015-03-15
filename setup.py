#!/usr/bin/env python2.7
import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_version(package):
    data = {}
    with open(os.path.join(package, '__init__.py'), 'r') as fd:
        exec(fd.read(), data)
    return data['__version__']


setup(
    name="pydidit",
    version=read_version("pydidit"),
    author="Valentine Gogichashvili",
    author_email="valgog@gmail.com",
    description=("A simple command line script to publish to iDoneThis"),
    license="BSD",
    keywords="todo idonethis",
    url="http://www.github.com/valgog/pydidit",
    py_modules=['pydidit'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Office/Business :: Scheduling",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
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
