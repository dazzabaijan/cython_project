import math
import time

def main(int nmax):
    
    cdef:
        double pi_by_four = 0.0
        double dx = 1.0/nmax
        int i

    t1 = time.perf_counter()
    
    for i in range(nmax):
        pi_by_four += math.sqrt(1 - (i*dx)**2)
    
    t2 = time.perf_counter()
    
    print(f"\nTime elapsed: {t2-t1:8.6f}s")
    
    pi = 4.0*pi_by_four*dx
    print(f"Pi = {pi:18.16f}")
    
    return t2-t1