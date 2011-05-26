#!/usr/bin/env python
#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Nicolas V custom edition):
# Nicolas V wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. But please say it's me that did it,
# because I seek for eternal glory. If we meet some day, and you think
# this stuff is funny, you can buy me a beer in return.
# ----------------------------------------------------------------------------
#

from distutils.core import setup

setup(name='Nobrainfuck',
      version='1.0',
      description='The sexiest programming language ever.',
      author='Nicolas V.',
      author_email='',
      url='https://github.com/nicolas-van/nbf',
      packages=[],
      py_modules = ['nobrainfuck', 'nobrainfuck_main', 'nbfparser'],
      requires=[
        "yapps2",
      ],
      scripts=['nobrainfuck'],
     )
