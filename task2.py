from functions import t_basis as tb
from functions import Hills_tensor as ht
import numpy as np

lya = 1
mu = 1
C1 = [lya+mu, 2*mu, lya, lya, 4*mu, lya+2*mu]
S1 = tb.inverse_tensor(C1)
multi = tb.t_multiply(C1, S1)

p_s, q_s = ht.get_hills_tensors_sphere(lya, mu)

print(C1)
print(S1)
print(p_s,q_s)
