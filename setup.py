#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='my-hotel-merger',
      version='0.0.1',
      description='A merging hotels tool that merges hotels data from different sources into a single source',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='duckien2346',
      url='https://github.com/duckien2346/my-hotel-merger',
      classifiers=[
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Programming Language :: Python :: 3 :: Only'
      ],
      python_requires=">=3.7,<3.13",
      install_requires=[
          'requests==2.32.*'
      ],
      extras_require={
          "test": [
              'pylint==2.12.*',
          ]
      },
      entry_points='''
          [console_scripts]
          my_hotel_merger=my_hotel_merger:main
      ''',
      packages=[
          'my_hotel_merger',
          'my_hotel_merger.models',
          'my_hotel_merger.repositories',
          'my_hotel_merger.services',
          'my_hotel_merger.utils'
      ]
      )
