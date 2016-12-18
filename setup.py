#!/usr/bin/python3
from setuptools import setup, find_packages
from codecs import open
from os import path
import pyATK

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=pyATK.__NAME__,
    version=pyATK.__VERSION__,
    packages=find_packages(),
    author_email=pyATK.__AUTHOR_EMAIL__,
    description=pyATK.__DESCRIPTION__,
    long_description=long_description,
    url='https://github.com/aturki/pyATK',
    license=pyATK.__LICENSE__,
    keywords='toolbox python library',
)
