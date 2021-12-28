import sys
from cython_project.cython_pi_calc import pi_calc1
from cython_project.cython_pi_calc import pi_calc2
from cython_project.cython_pi_calc import pi_calc3
import pi_calc4_omp

if int(len(sys.argv)) == 3:
    # normal python
    TE1 = pi_calc1.main(int(sys.argv[1]))
    
    # cython 1
    TE2 = pi_calc2.main(int(sys.argv[1]))
    print(f'Cython 1 is {TE1/TE2:2f} times faster.')
    
    # cython 2
    TE3 = pi_calc3.main(int(sys.argv[1]))
    print(f'Cython 2 is {TE1/TE3:2f} times faster.')
    
    # cython omp
    TE4 = pi_calc4_omp.main(int(sys.argv[1]), int(sys.argv[2]))
    print(f'Cython OpenMP is {TE1/TE4:2f} times faster.')
    
else:
    print(f"Usage: {sys.argv[0]} <ITERATIONS> <THREADS>")