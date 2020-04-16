# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:56:24 2020

@author: dujing1107
"""
import numpy as np
import matplotlib.pyplot as plt

# iteration period
T = 30
#Population 
N0 = 127749000

N = np.zeros(T) # total number
S = np.zeros(T) # Susceptible people
E = np.zeros(T) # Infected people but in incubation period
Eq = np.zeros(T) # Isolated and infected people in incubation period
Sq = np.zeros(T) # Isolated and susceptible people and isolated
I = np.zeros(T) # Infected people with symptons  
R = np.zeros(T) # recovered people
H = np.zeros(T) # Isolated and infected people with symptons  
D = np.zeros(T) # died



c = 2 #The contact rate
v = 1/14  #The rate of releasing form being isolated
iso = 0.000001 #The isolation rate of people who didn't have infection symptons
iso_i = 0.037 #The isolation rate of people who already have infection symptons
b = 0.00000000205 #The infection rate of COVID-19
r = 0.014  #The cure rate of people who are not isolated
iso_r = 0.07 #The cure rate of people who were isolated already
d = 0.00027 #The death rate
s = 1/7 #The possibility of people geting infection symptoms during incubation period who haven't been isolated
iso_s = 0.13 #The possibility of people geting infection symptoms during incubation period who haven been isolated

N[0] = N0
E[0] = 1290
S[0] = N[0] - E[0] - I[0] - R[0] - D[0] - Sq[0] -Eq[0]
I[0] = 1594
Eq[0] = 2107
Sq[0] = 29895
H[0] = 60
R[0] = 456
D[0] = 57

t = np.arange(0, T)
for i in range(1,T):
    dS = v*Sq[i-1] - (I[i-1]+E[i-1])*S[i-1]*c*(iso*(1-b) + b)
    S[i] = S[i-1] + dS
    dE = b*(I[i-1]+E[i-1])*S[i-1]*(1-iso)*c -E[i-1]*s - r*E[i-1]
    E[i] = E[i-1] + dE
    dI = E[i-1]*s - I[i-1]*iso_i - I[i-1]*r - I[i-1]*d
    I[i] = I[i-1] + dI
    dR = I[i-1]*r + r*E[i-1] + H[i-1]*iso_r + Eq[i-1]*iso_r
    R[i] = R[i-1] + dR 
    dSq = (I[i-1]+E[i-1])*S[i-1]*c*iso*(1-b) - v*Sq[i-1]
    Sq[i] = Sq[i-1] + dSq
    dEq = (I[i-1]+E[i-1])*b*c*iso*S[i-1] - Eq[i-1]*iso_s - Eq[i-1]*iso_r
    Eq[i] = Eq[i-1] + dEq
    dH = Eq[i-1]*iso_s + I[i-1]*iso_i - H[i-1]*d - H[i-1]*iso_r
    H[i] = H[i-1] + dH
    dD = H[i-1]*d + I[i-1]*d
    D[i] = D[i-1] + dD
    N[i] = S[i] + E[i] + I[i] + R[i] + D[i] + Eq[i] + Sq[i]

    

#plot 

fig, axs = plt.subplots(2, 2)
grid = plt.GridSpec(2, 2)
ax1 = plt.subplot(grid[:])

ax1.plot(t, E+Eq, color = 'orange', linewidth = 2, label = 'Patients in incubation period')
ax1.plot(t, I, color = 'red', linewidth = 2, label = 'Patients infected with symptoms')
ax1.plot(t, D, color = 'black', linewidth = 2, label = 'Deceased')
ax1.plot(t, H, color = 'blue', linewidth = 2, label = 'Patients that can be treated in hospital')
ax1.set_xlim([0, 30])
ax1.grid()
ax1.set_title('Incubated, Infected with Symptoms, Deceased')
ax1.legend(loc='upper left', fontsize=10)                    










