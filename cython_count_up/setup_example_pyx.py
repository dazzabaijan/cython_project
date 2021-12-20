from Cython.Build.Dependencies import cythonize
from distutils.core import setup
from Cython.Build import Cythonize

setup(name='example_cy',
      ext_modules=cythonize('example_cy.pyx'))