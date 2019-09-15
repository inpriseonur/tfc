#!/usr/bin/env python3

import tfc

from setuptools import setup

setup(name='tfc',
      version='0.1.0',
      description='Simple Translate App From Clipboard',
      long_description=open('README.md').read(),
      author='Yunus Emre Geldegul',
      author_email='yunusemregeldegul@gmail.com',
      url='http://github.com/emregeldegul/tfc',
      packages=['tfc'],
      entry_points={
        'console_scripts': [
          'tfc = tfc:main',
        ]
      },
      license='Apache License 2.0'
      )