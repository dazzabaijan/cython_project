from Cython.Build.Dependencies import cythonize
from distutils.core import setup

setup(name='example_cy',
      ext_modules=cythonize('example_cy.pyx'))