from scipy.integrate import dblquad
area = dblquad(lambda y, x: x+y, 1, 2, lambda x:x, lambda x:2*x)
print(area)
