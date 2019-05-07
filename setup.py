#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='jelasticli',
      version='0.0.0',
      description='jelasticli - A Jelastic API client',
      author='Didier \'OdyX\' Raboud',
      author_email='odyx@liip.ch',
      url='https://github.com/liip/jelasticli',
      install_requires=[
          'requests',
      ],
      dependency_links=[
      ],
      packages=find_packages()
      )
