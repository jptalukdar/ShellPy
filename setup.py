#!/usr/bin/env python
import os
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(name='ShellPy',
      version='0.1.1',
      description='',
      long_description=README,
      long_description_content_type='text/markdown',
      packages=['ShellPy'],
      author='Jyotiplaban Talukdar',
      author_email='Jyotiplaban@gmail.com',
      url="https://github.com/jptalukdar/ShellPy",
      license="MIT",
      classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
      install_requires=[],
      zip_safe=False)
