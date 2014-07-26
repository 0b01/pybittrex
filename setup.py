#!/usr/bin/env python

from distutils.core import setup


setup(name='pybittrex',
      version='0.1',
      packages=['pybittrex'],
      modules=[
          'pybittrex'
      ],
      description='Python bindings for bittrex API v1.1.',
      author='Ricky Han',
      author_email='ricky@han.org',
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: MIT License',
          'Development Status :: 3 - Alpha',
          'Topic :: Office/Business :: Financial',
      ])
