import librosa
import librosa.display
import numpy as np
from mpl_toolkits import mplot3d

import matplotlib.pyplot as plt


y, sr = librosa.load("healthy1s1.mp3")
D = librosa.stft(y, hop_length=128)

plt.figure()
ax = plt.axes(projection='3d')

x, y, z = [], [], []
for i, a in enumerate(D[:-600]) :
    for j, b in enumerate(np.abs(a)):
        x.append(i)
        y.append(j)
        z.append(b)
ax.plot3D(y, x, z)

plt.figure()
librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

y, sr = librosa.load("ill1s1.mp3")
D = librosa.stft(y, hop_length=128)



plt.figure()
ax = plt.axes(projection='3d')

x, y, z = [], [], []
for i, a in enumerate(D[:-600]) :
    for j, b in enumerate(np.abs(a)):
        x.append(i)
        y.append(j)
        z.append(b)
ax.plot3D(y, x, z)

plt.figure()
librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')
plt.show()
