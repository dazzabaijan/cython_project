import timeit

cy = timeit.timeit('example_cy.test(500000)', setup='import example_cy', number=1000)
py = timeit.timeit('example_py.test(500000)', setup='import example_py', number=1000)

print(cy, py)
print(f'Cython is {py/cy:2f} times faster.')