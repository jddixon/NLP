#!/usr/bin/python3

# nlp/setup.py

""" Set up NLP package. """

import re
from distutils.core import setup
__version__ = re.search(r"__version__\s*=\s*'(.*)'",
                        open('src/nlp/__init__.py').read()).group(1)

# see http://docs.python.org/distutils/setupscript.html

setup(name='nlp',
      version=__version__,
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      py_modules=[],
      packages=['src/nlp'],
      # following could be in scripts/ subdir
      scripts=[],
      description='some natural language processing (NLP) tools',
      url='https://jddixon.github.io/nlp',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      )
