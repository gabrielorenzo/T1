============================================

## Nom i cognoms: Gabriel Lorenzo Felix



## Representació temporal i freqüencial de senyals d'àudio.

### Domini temporal

Per llegir, escriure i representar un fitxer en format `*.wav` en python podem fem servir els següents mòduls:

- Numpy:
```python
import numpy as np
```
- Matplotlib: 
```python
import matplotlib.pyplot as plt
```
- Soundfile:
```python
import soundfile as sf
```

Per **crear** i **guardar** a un fitxer un senyal sinusoidal de freqüència `fx Hz`, digitalitzat a `fm Hz`, de durada `T` segons i amplitud 
`A` fem:

```python
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav
```

El resultat és un fitxer guardat al directori de treball i que es pot reproduir amb qualsevol reproductor d'àudio

Per **representar** gràficament 5 períodes de senyal fem:

```python
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 
```

El resultat del gràfic és:

<img src="img/sinusoide.png" width="480" align="center">

> Nota: Si es treballa amb ipython, es pot escriure %matplotlib i no cal posar el plt.show() per veure gràfics

El senyal es pot **escoltar (reproduir)** directament des de python important un entorn de treball amb els dispositius de so, com per 
exemple `sounddevice`:

```python
import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                # Reproducció d'àudio
```

### Domini transformat

Domini transformat. Els senyals es poden analitzar en freqüència fent servir la Transformada Discreta de Fourier. 

La funció que incorpora el paquet `numpy` al submòdul `fft` és `fft`:

```python
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide
```

I podem representar el mòdul i la fase, en funció de la posició de cada valor amb:

```python
k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics
```

<img src="img/TF.png" width="480" align="center">

Proves i exercicis a fer i entregar
-----------------------------------

1. Reprodueix l'exemple fent servir diferents freqüències per la sinusoide. Al menys considera $f_x = 4$ kHz, a banda d'una
    freqüència pròpia en el marge audible. Comenta els resultats.

```python
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
```
<img src="img/1.1.png" width="480" align="center">
<img src="img/1.1.2.png" width="480" align="center">

- La frecuencia de 4000 Hz a pesar de que la generamos no aparece en la gráfica. Esto se debe al fenómeno de Nyquist.

2. Modifica el programa per considerar com a senyal a analitzar el senyal del fitxer wav que has creat 

    (`x_r, fm = sf.read('nom_fitxer.wav')`).

```python
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
```

- Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.

<img src="img/2.1.png" width="480" align="center">
<img src="img/2.1.2.png" width="480" align="center">

- Explica el resultat del apartat anterior.

    - Se obtiene el mismo resultado que en el apartado anterior, la unica diferencia es que necesitamos conocer el valor de la frecuencia de la sinusoide menor.

3. Modifica el programa per representar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en el marge de
    $0$ a $f_m/2$ en Hz.

> NOTES:
>
> - Per representar en dB has de fer servir la fórmula següent:
>
> $X_{dB}(f) = 20\log_{10}\left(\frac{\left|X(f)\right|}{\max(\left|X(f)\right|}\right)$
>
> - La relació entre els valors de l'índex k i la freqüència en Hz és:
>
> $f_k = \frac{k}{N} f_m$

```python
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
```

- Comprova que la mesura de freqüència es correspon amb la freqüència de la sinusoide que has fet servir.

<img src="img/3.1.png" width="480" align="center">


4. Tria un fitxer d'àudio en format wav i mono (el pots aconseguir si en tens amb altres formats amb el programa Audacity). 
    Llegeix el fitxer d'àudio i comprova:

```python
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
```

- Freqüència de mostratge.

```python
print('Frecuencia del señal:', fm, 'Hz')
```
    - La freqüència de mostratge es de 48000 Hz

- Nombre de mostres de senyal.

```python
print('Muestras del señal:', len(x))
```
    - La senyal te 96001 mostres

- Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.

<img src="img/4.1.png" width="480" align="center">

Entrega
-------

- L'alumne ha de respondre a totes les qüestions formulades en aquest mateix fitxer, README.md.
    - El format del fitxer es l'anomenat *Markdown* que permet generar textos amb capacitats gràfiques (com ara *cursiva*, **negreta**,
      fòrmules matemàtiques, taules, etc.), sense perdre la llegibilitat en mode text.
    - Disposa d'una petita introducció a llenguatge de Markdown al fitxer `MARKDOWN.md`.
- El repositori GitHub ha d'incloure un fitxer amb tot el codi necesari per respondre les qüestions i dibuixar les gràfiques.
- El nom del fitxer o fitxers amb el codi ha de començar amb les inicials de l'alumne (per exemple, `fvp_codi.py`).
- Recordéu ficar el el vostre nom complet a l'inici del fitxer o fitxers amb el codi i d'emplar el camp `Nom i cognoms` a dalt de tot
  d'aquest fitxer, README.md.
