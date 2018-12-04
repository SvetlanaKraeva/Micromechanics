from functions import t_basis as tb
from functions import Hills_tensor as ht
from functions import effective_field as ef
import matplotlib.pyplot as plt
import numpy as np

p1 = np.linspace(0, 0.5, 11)
p2 = np.linspace(0, 0.5, 11)
p_star = 0.05

lambda0 = 1
mu0 = 1
C0 = tb.get_C(lambda0, mu0)
S0 = tb.inverse_tensor(C0)

lambda1 = 2
mu1 = 2
C1 = tb.get_C(lambda1, mu1)
S1 = tb.inverse_tensor(C1)

lambda2 = 1.5
mu2 = 1.5
C2 = tb.get_C(lambda2, mu2)
S2 = tb.inverse_tensor(C2)

p_d, q_d = ht.get_hills_tensors_disk(lambda1, mu1)
p_s, q_s = ht.get_hills_tensors_sphere(lambda2, mu2)

S_star1 = S0[5]+p1*ef.property_contribution_tensor(S0, S1, q_d)[5]+p2*ef.property_contribution_tensor(S0, S2, q_s)[5]
S_star1 = S_star1/S0[5]

S_star2 = S0[5]+p1*ef.property_contribution_tensor(S0, S1, q_d)[5]+p_star*ef.property_contribution_tensor(S0, S2, q_s)[5]
S_star2 = S_star2/S0[5]

S_sphere = S0+p_star*ef.property_contribution_tensor(S0, S2, q_s)
S_star3 = S_sphere[5]+p1*ef.property_contribution_tensor(S_sphere, S1, q_d)[5]
S_star3 = S_star3/S0[5]

plt.plot(p1, S_star1, label="$p_1$ = $p_2$")
plt.plot(p1, S_star2, label="$p_2$ - fixed")
plt.plot(p1, S_star3, label="spheres first")
plt.axvline(x=p_star, color='black', linestyle='--')
plt.legend()
plt.axis('equal')
plt.xlabel('density $p_1$')
plt.ylabel(r'${S*/S_0}$')
plt.show()

