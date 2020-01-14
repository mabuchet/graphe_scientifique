# -*- coding: utf-8 -*-

""" BUT : 
Script pour tracer des fonctions de manière lisible à destination d'un document
scientifique.

La fonction choisie ici correspond à la représentation des pseudo-oscillations
d'un oscillateur amorti en régime pseudo-périodique en fonction des paramètres
omega_0 (pulsation propre) et Q (facteur de qualité).

Auteur : Marc-Antoine BUCHET
Date : 08/01/2020
"""

import numpy as np
import matplotlib.pyplot as plt

##############################################################################
# Paramétrage des graphs :
##############################################################################   
font = {'family' : 'sans',
        'weight' : 'bold',
        'size'   : 18}
plt.rc('font', **font)

lines = {'linewidth' : 2.0,
         'markeredgewidth' : 2.0,
         'markersize' : 10.0}
plt.rc('lines', **lines)

plt.ion() # activation du mode interactif

plt.close('all') # fermeture des figures éventuellement ouvertes

##############################################################################
# Paramètres physiques : 
##############################################################################
omega_0 = 10. # rad/s
Q = 10. 
tau = 2*Q/omega_0 # temps d'amortissement
Omega = omega_0/(2*Q)*np.sqrt(4*Q**2-1)
E_0 = 5. # V ; Tension initiale
A = E_0
B = E_0/(Omega*tau)

##############################################################################
# Paramètres pour les graphiques : 
##############################################################################
t_min = 0.
t_max = 5.*tau
N = 10000 # nombre de point pour les graphs
t = np.linspace(t_min,t_max,N)

##############################################################################
# Fonctions à tracer : 
##############################################################################
def u_c(t) :
    """  Fonction qui prend en entrée un réel ou un tableau numpy de réels et
    renvoit un réel ou un tableau numpy de réels représentatif de la tension aux
    bornes d'un condensateur dans un circuit RLC série en régime libre avec la 
    condition initiale u_C(0) = E_0
    """
    return np.exp(-t/tau)*(A*np.cos(Omega*t)+B*np.sin(Omega*t))

def e_plus(t) :
    """
    Enveloppe exponentielle supérieure.
    """
    return np.exp(-t/tau)*np.sqrt(A**2+B**2)

def e_moins(t) :
    """
    Enveloppe exponentielle intérieure.
    """
    return -e_plus(t)


##############################################################################
# Graphe : 
##############################################################################
x=t

# u_C(t) :
y=u_c(t)
label = 'u_C(t)'
plt.plot(x,y,label=label)

# Enveloppe exponentielle supérieure :
y=e_plus(t)
label = 'e_+(t)'
plt.plot(x,y,'--',label=label)

# Enveloppe exponentielle inférieure :
y=e_moins(t)
label = 'e_-(t)'
plt.plot(x,y,':',label=label)

# Abscisse et ordonnée :
plt.xlabel('temps (s)')
plt.ylabel('tension (V)')

# Affichage grille et légende :
plt.legend()
plt.grid()
plt.tight_layout()