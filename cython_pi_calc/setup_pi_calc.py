from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(name='pi_calc1',
      ext_modules=cythonize('pi_calc1.pyx'))

setup(name='pi_calc2',
      ext_modules=cythonize('pi_calc2.pyx'))

setup(name='pi_calc3',
      ext_modules=cythonize('pi_calc3.pyx'))

ext_modules = [
    Extension(
        "pi_calc4_omp",
        ["pi_calc4_omp.pyx"],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],
    )
]

setup(name="pi_calc4_omp",
      ext_modules=cythonize(ext_modules))