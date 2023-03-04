import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft

# Llegim la senyal
x, fm = sf.read('beethoven5thsymphony.wav')

muestra_tot = fm * 2                   
muestra_inicio = fm * 6                  
muestra_fin = muestra_inicio + muestra_tot + 1  

x = x[muestra_inicio : muestra_fin : 1]   

print('Frecuencia del señal:', fm, 'Hz')

print('Muestras del señal:', len(x))

L = int(len(x))                       
Tm=1/fm                               
t=Tm*np.arange(L)                     

Ls=int(fm*0.025)                      

# Representació temporal
plt.figure(5)                         
plt.plot(t[0:Ls], x[0:Ls])            
plt.xlabel('t en segundos')             
plt.title('25ms de la senyal')        
plt.show()                            

N = 5000                              
X=fft(x[0 : Ls], N)                   

X = X[0 : int(N/2)]

# Fem cambis d'escala
Xmax=float(max(abs(X)))               
Xabs=20*np.log10((abs(X)/Xmax))      

k=np.arange(int(N/2))                 
freq=(k/N)*fm                         

# Mostrem la transformada
plt.figure(6)                         
plt.subplot(211)                      
plt.plot(freq,Xabs)                   
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|dB')                
plt.subplot(212)                      
plt.plot(freq,np.unwrap(np.angle(X))) 
plt.xlabel('Hz')                      
plt.ylabel('$\phi_x[k]$')             
plt.show()                     