import numpy as np
import matplotlib.pyplot as plt

"constituent 1"
k1 = 1
"constituent 2"
k2 = 2
"[k]=k2-k1"
dk = k2-k1
p = np.linspace(0, 1, 11)
"<k>=p1*k1+p2*k2"
k_v = (1-p)*k1+p*k2

Kv = (1-p)+p*k2/k1
Kr = 1/((1-p)+p*k1/k2)

KHSm = k_v-((1-p)*p*dk**2)/(3*k2-p*dk)
KHSp = k_v-((1-p)*p*dk**2)/(3*k2+p*dk)

Ka = (1-(1-p)*p/3*((dk/k_v)**2))*k_v/k1


plt.plot(p, Kv, label="Voigt")
plt.plot(p, Kr, label="Reuss")
plt.plot(p, KHSm, label="Hashin-Shtrikman-")
plt.plot(p, KHSp, label="Hashin-Shtrikman+")
plt.plot(p, Ka, label="Second-order approximation")
plt.legend()
plt.axis('equal')
plt.xlabel('density $p_2$')
plt.ylabel(r'${k*/k_0}$')
plt.show()