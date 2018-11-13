from functions import t_basis as tb


lya = 1
mu = 1
C1 = [lya+mu, 2*mu, lya, lya, 4*mu, lya+2*mu]
S1 = tb.inverse_tensor(C1)
print(C1)
print(S1)
multi = tb.t_multiply(C1,S1)
print(multi)