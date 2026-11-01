import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

plt.figure(figsize=(16, 6))

##################
# Bode Theorique #
##################

# Constantes du système


k = 12 # 8 
Mb = 0.744
mp = 0.131
L = 0.54 
alpha = 0.094
gamma = 0.05 #2.17E-3
g = 9.81

# Définition du numérateur et du dénominateur avec le pendule

numTMD = [k*mp*L**2,  #p^2
       k*gamma,  #p^1
       k*mp*g*L]  #p^0

denomTMD = [Mb*mp*L**2,  #p^4
         (Mb+mp)*gamma+alpha*mp*L**2,  #p^3
         (Mb+mp)*mp*g*L+alpha*gamma+k*mp*L**2,  #p^2
         alpha*mp*g*L + k*gamma,  #p^1
         k*mp*g*L]  #p^0

# Définition du numérateur et du dénominateur sans le pendule (mp=0)

num_noTMD = [k]

denom_noTMD = [Mb,  #p^3
               alpha,  #p^2
               k]  #p^1

# Création de la fonction de transfert

ft_TMD = signal.lti(numTMD, denomTMD)
ft_noTMD = signal.lti(num_noTMD, denom_noTMD)

# Calcul du diagramme de Bode

freq = np.logspace(-0.5, 0.1, 1000) #1000 valeurs entre 10^(-0.5) et 10^(0.1)
omega = 2*np.pi*freq
wTMD, magTMD, phaseTMD = signal.bode(ft_TMD, w=omega)
w_noTMD, mag_noTMD, phase_noTMD = signal.bode(ft_noTMD, w=omega)

# Affichage
plt.title('Diagramme de Bode')
plt.semilogx(wTMD/(2*np.pi),  magTMD, color='c', lw=2, label = 'Bode théorique avec pendule')    # Amplitude + (line width = 2 points)
plt.semilogx(w_noTMD/(2*np.pi) , mag_noTMD, color='tomato', lw=2, label = 'Bode théorique sans pendule')    # Amplitude + (line width = 2 points)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(which='both')



#####################
# Bode Experimental #
#####################

#on ouvre le fichier avec des donnes experimentales
raw_data_noTMD = open("bode_modif_noTMD.txt", 'r')
data_noTMD = raw_data_noTMD.readlines()

frequence_noTMD = []
amplitude_noTMD = []
phase_noTMD = []


# On complete les listes au dessus avec des donnees
for i in range(1, len(data_noTMD)):
    lignei = data_noTMD[i].strip('\n')
    ligne2 = lignei.split('\t')
    frequence_noTMD.append(float(ligne2[0]))
    amplitude_noTMD.append(float(ligne2[1]))
    phase_noTMD.append(float(ligne2[2]))

raw_data_noTMD.close()


# on convertit dans les dB
amplitude_dB_noTMD = 20 * np.log10(amplitude_noTMD)


#Idem mais avec des donnees avec le pendule
raw_data = open("bode_TMD_sorted.txt", 'r')
data = raw_data.readlines()

frequence = []
amplitude = []
phase = []

for i in range(1, len(data)):
    lignei = data[i].strip('\n')
    ligne2 = lignei.split('\t')
    frequence.append(float(ligne2[0]))
    amplitude.append(float(ligne2[1]))
    phase.append(float(ligne2[2]))

raw_data.close()

# on convertit dans les dB
amplitude_dB = 20 * np.log10(amplitude)


# amplitude

plt.semilogx(frequence_noTMD, amplitude_dB_noTMD, 'o:', color='red', label = 'Bode expérimental sans pendule', linewidth=2, markersize=4)
plt.semilogx(frequence, amplitude_dB,'o:', color='blue', label = 'Bode expérimental avec pendule', linewidth=2, markersize=4)
plt.axhline(y=0, color='black', linestyle='--', alpha=0.5)
plt.grid(True, alpha=0.3)
plt.ylabel('Amplitude (dB)', fontsize=12) 
plt.title('Diagramme de Bode', fontsize=14) 
plt.legend()

plt.subplots_adjust(left=0.07,    
                    bottom=0.10, 
                    right=0.95,   
                    top=0.92)

#plt.savefig('bode_diagramme_k=12_gamma=0.05.png', dpi=300)
plt.show()