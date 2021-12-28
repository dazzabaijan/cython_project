import sys
import time
from cython_project.cython_count_up import example_cy
import example_py

if int(len(sys.argv)) == 2:
    # normal python
    time_start = time.perf_counter()
    TE1 = example_py.test(int(sys.argv[1]))
    time_end = time.perf_counter()
    t1 = time_start - time_end
    
    # cython 1
    time_start = time.perf_counter()
    TE2 = example_cy.test(int(sys.argv[1]))
    time_end = time.perf_counter()
    t2 = time_start - time_end
    print(f'Cython is {t1/t2:2f} times faster.')
    
else:
    print(f"Usage: {sys.argv[0]} <ITERATIONS>")