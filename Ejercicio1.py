import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft

# Generamos la senyal
T= 2.5
fm=8000
fx1=440
fx2=4000
fx3=220
A=0.5
pi=np.pi
L = int(fm * T)
Tm=1/fm
t=Tm*np.arange(L)
x = A * ( np.cos(2*pi*fx1*t) + np.sin(2*pi*fx2*t) + np.cos(2*pi*fx3*t) ) 
sf.write('so_ej1.wav', x, fm)

# Representamos la senyal
Tx=1/fx3
Ls=int(fm*5*Tx)

plt.figure(0)
plt.plot(t[0:Ls], x[0:Ls])
plt.xlabel('t en segundos')
plt.title('5 periodos') 
plt.show()

# Escuchamos la senyal
sd.play(x,fm)

# Generamos la transformada
N=5000
X=fft(x[0 : Ls], N)

# Mostramos la trasnformada
k=np.arange(N)

plt.figure(1)                         
plt.subplot(211)                      
plt.plot(k,abs(X))                    
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                  
plt.subplot(212)                     
plt.plot(k,np.unwrap(np.angle(X)))    
plt.xlabel('Index k')                 
plt.ylabel('$\phi_x[k]$')             
plt.show()