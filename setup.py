#!/usr/bin/env python
from setuptools import setup, find_packages
import codes
import os
import re
import compiling

here = os.path.abspath(os.path.dirname(__file__))

with codes.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with codes.open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirement = f.read()

setup(
    name='compiling',
    version=compiling.__version__,
    description='Compiling message generator',
    long_description=long_description,
    url='https://github.com/hacking-thursday/compiling',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='compile',
    install_requires=requirement,
    package_data={
    },
    data_files=[
    ],
    entry_points={
        'console_scripts': [
            'bin/compiling',
        ],
    },
)
