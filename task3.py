from functions import t_basis as tb
from functions import Hills_tensor as ht
from functions import effective_field as ef
import matplotlib.pyplot as plt
import numpy as np

lambda_medium = 1
mu_medium = 1

lambda_inclusion = 1.5
mu_inclusion = 1.5

inclusion_concentration = np.linspace(0, 1, 21)

C_medium = tb.get_C(lambda_medium, mu_medium)
C_inclusion = tb.get_C(lambda_inclusion, mu_inclusion)

p_inclusion, q_inclusion = ht.get_hills_tensors_disk(lambda_inclusion, mu_inclusion)
p_texture1, q_texture1 = ht.get_hills_tensors_sphere(lambda_medium, mu_medium)
p_texture2, q_texture2 = ht.get_hills_tensors_disk(lambda_medium, mu_medium)

C_effective1 = []
C_effective2 = []
for i in np.nditer(inclusion_concentration):
    C_e1 = C_medium+i*tb.inverse_tensor(tb.inverse_tensor(C_inclusion-C_medium)+p_inclusion-i*p_texture1)
    C_effective1.append(C_e1[5]/C_medium[5])
    C_e2 = C_medium + i * tb.inverse_tensor(tb.inverse_tensor(C_inclusion - C_medium) + p_inclusion - i * p_texture2)
    C_effective2.append(C_e2[5]/C_medium[5])

C_effective_non_iter = 1+inclusion_concentration*ef.property_contribution_tensor(
    C_medium, C_inclusion, p_inclusion)[5]/C_medium[5]

plt.plot(inclusion_concentration, C_effective1, label="P(alpha) - spheres")
plt.plot(inclusion_concentration, C_effective2, label="P(alpha) - ellipsoids")
plt.plot(inclusion_concentration, C_effective_non_iter, label="Non-interaction approximation")
plt.axis('equal')
plt.legend()
plt.xlabel('density of inclusions')
plt.ylabel(r'${C*/C_0}$')
plt.show()

