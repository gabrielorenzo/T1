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

plt.figure(0)
plt.plot(t[0:Ls], x[0:Ls])
plt.xlabel('t en segundos')
plt.title('5 periodos') 
plt.show()

# Reproducimos el señal
sd.play(x,fm)

# Generamos la transformada
N=5000
X=fft(x[0 : Ls], N)

# Mostramos la transformada
k=np.arange(N)

plt.figure(1)                     
plt.subplot(211)                    
plt.plot(k,abs(X))                    
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                  #
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X))) 
plt.xlabel('Index k')
plt.ylabel('$\phi_x[k]$')
plt.show()