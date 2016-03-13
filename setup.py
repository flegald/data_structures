# -*- coding: utf-8 -*-
"""Setup for data_structures package."""

from setuptools import setup


setup(name='data structures',
      description='Collection of data structures creatd in Python.',
      version=0.1,
      keywords=[],
      classifiers=[],
      author='Ben Garnaat',
      author_email='',
      license='MIT',
      packages=[],  # all your python packages with an __init__ file
      py_modules=['Node',
                  'linked_list',
                  'double_link',
                  'stack',
                  'Queue',
                  'parenthetics',
                  ],  # your python modules to include
      package_dir={'': 'src'},
      install_requires=[],
      extras_require={'test': ['pytest', 'pytest-xdist', 'tox']}
      )
