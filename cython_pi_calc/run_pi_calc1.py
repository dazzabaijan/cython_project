import sys
import pi_calc1

if int(len(sys.argv)) == 2:
    pi_calc1.main(int(sys.argv[1]))
else:
    print(f"Usage: {sys.argv[0]} <ITERATIONS>")