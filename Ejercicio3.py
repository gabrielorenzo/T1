import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft

# Leemos el señal
x, fm = sf.read('so_ej1.wav')

L = int(len(x))                     
Tm=1/fm                              
t=Tm*np.arange(L)                    


Tx=1/220                             
Ls=int(fm*5*Tx)                      

# Generamos la transformada
N=5000                               
X=fft(x[0 : Ls], N)                  

# Cambios de escala
Xmax=float(max(abs(X)))              
Xabs=20*np.log10((abs(X)/Xmax))      

k=np.arange(N)                       
freq=(k/N)*fm

# Mostramos la transformada
plt.figure(4)                       
plt.subplot(211)                     
plt.plot(freq,Xabs)                  
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|dB')               
plt.subplot(212)               
plt.plot(freq,np.unwrap(np.angle(X)))   
plt.xlabel('Hz')                     
plt.ylabel('$\phi_x[k]$')           
plt.show()                          