#!/usr/bin/env python

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='CG_SimTool',
    version='0.1',
    description='Under construction',
    url='https://github.com/aaguirre-rdit/CG_SimTool',
    author='Anne Aguirre',
    author_email='aaguirre.rdit.at.gmail.com',
    license='MIT',
    keywords="LAMMPS, LLPS",
    python_requires='>=3.6',
    packages=find_packages(),
)
