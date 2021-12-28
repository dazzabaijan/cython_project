from libc cimport math
from cython.parallel cimport prange
import time
cimport openmp

def main(int nmax, int threads):

    cdef:
        double pi_by_four = 0.0
        double dx = 1.0/nmax
        double initial, final
        int i

    print(f"\nThreads set to {threads:2d}")

    t1 = openmp.omp_get_wtime()
    
    for i in prange(nmax, nogil=True, num_threads=threads):
        pi_by_four += math.sqrt(1 - (i*dx)**2)
    
    t2 = openmp.omp_get_wtime()
    
    print(f"Elapsed time: {t2-t1:8.6f}s")

    pi = 4.0*pi_by_four*dx
    print(f"Pi = {pi:18.16f}")
    
    return t2-t1

