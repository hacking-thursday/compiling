#!/usr/bin/env python
from distutils.core import setup

import os

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    req = f.read()

setup(
    name='compiling',
    version='0.0.0',
    description='Compiling message generator',
    long_description=open('README.md').read(),
    install_requires=req
    scripts=['bin/compiling'],
    url='https://github.com/hacking-thursday/compiling',
)
