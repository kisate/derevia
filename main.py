import librosa
import librosa.display
import numpy as np
y1, sr1 = librosa.load("healthy1s1.mp3")
D1 = librosa.stft(y1, hop_length=128)
y2, sr2 = librosa.load("healthy1s2.mp3")
D2 = librosa.stft(y2, hop_length=128)
y3, sr3 = librosa.load("healthy1s3.mp3")
D3 = librosa.stft(y3, hop_length=128)
y4, sr4 = librosa.load("healthy1s4.mp3")
D4 = librosa.stft(y4, hop_length=128)


for d in [D1, D2, D3, D4] :
    for i, x in enumerate(d) :
        if i < 0 : d[i] = [0]*len(x)

import matplotlib.pyplot as plt

plt.figure()
plt.subplot(4, 1, 1)

librosa.display.specshow(librosa.amplitude_to_db(D1, ref=np.max, ), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 2)

librosa.display.specshow(librosa.amplitude_to_db(D2, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')


plt.subplot(4, 1, 3)

librosa.display.specshow(librosa.amplitude_to_db(D3, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 4)

librosa.display.specshow(librosa.amplitude_to_db(D4, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

y1, sr1 = librosa.load("ill4s1.mp3")
D1 = librosa.stft(y1, hop_length=128)
y2, sr2 = librosa.load("ill4s2.mp3")
D2 = librosa.stft(y2, hop_length=128)

y3, sr3 = librosa.load("ill4s3.mp3")
D3 = librosa.stft(y3, hop_length=128)
y4, sr4 = librosa.load("ill4s4.mp3")
D4 = librosa.stft(y4, hop_length=128)

for d in [D1, D2, D3, D4] :
    for i, x in enumerate(d) :
        if i < 0 : d[i] = [0]*len(x)

print(D2[1])

plt.figure()
plt.subplot(4, 1, 1)

librosa.display.specshow(librosa.amplitude_to_db(D1, ref=np.max, ), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 2)

librosa.display.specshow(librosa.amplitude_to_db(D2, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 3)

librosa.display.specshow(librosa.amplitude_to_db(D3, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 4)

librosa.display.specshow(librosa.amplitude_to_db(D4, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

y1, sr1 = librosa.load("ill3s1.mp3")
D1 = librosa.stft(y1, hop_length=128)
y2, sr2 = librosa.load("ill3s2.mp3")
D2 = librosa.stft(y2, hop_length=128)

y3, sr3 = librosa.load("ill3s3.mp3")
D3 = librosa.stft(y3, hop_length=128)
y4, sr4 = librosa.load("ill3s4.mp3")
D4 = librosa.stft(y4, hop_length=128)

for d in [D1, D2, D3, D4] :
    for i, x in enumerate(d) :
        if i < 0 : d[i] = [0]*len(x)

print(D2[1])

plt.figure()
plt.subplot(4, 1, 1)

librosa.display.specshow(librosa.amplitude_to_db(D1, ref=np.max, ), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 2)

librosa.display.specshow(librosa.amplitude_to_db(D2, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 3)

librosa.display.specshow(librosa.amplitude_to_db(D3, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 4)

librosa.display.specshow(librosa.amplitude_to_db(D4, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

y1, sr1 = librosa.load("healthy2s1.mp3")
D1 = librosa.stft(y1, hop_length=128)
y2, sr2 = librosa.load("healthy2s2.mp3")
D2 = librosa.stft(y2, hop_length=128)

y3, sr3 = librosa.load("healthy2s3.mp3")
D3 = librosa.stft(y3, hop_length=128)
y4, sr4 = librosa.load("healthy2s4.mp3")
D4 = librosa.stft(y4, hop_length=128)

for d in [D1, D2, D3, D4] :
    for i, x in enumerate(d) :
        if i < 0 : d[i] = [0]*len(x)

print(D2[1])

plt.figure()
plt.subplot(4, 1, 1)

librosa.display.specshow(librosa.amplitude_to_db(D1, ref=np.max, ), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 2)

librosa.display.specshow(librosa.amplitude_to_db(D2, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 3)

librosa.display.specshow(librosa.amplitude_to_db(D3, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 4)

librosa.display.specshow(librosa.amplitude_to_db(D4, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

y1, sr1 = librosa.load("healthy3s1.mp3")
D1 = librosa.stft(y1, hop_length=128)
y2, sr2 = librosa.load("healthy3s2.mp3")
D2 = librosa.stft(y2, hop_length=128)

y3, sr3 = librosa.load("healthy4s1.mp3")
D3 = librosa.stft(y3, hop_length=128)
y4, sr4 = librosa.load("healthy4s2.mp3")
D4 = librosa.stft(y4, hop_length=128)

for d in [D1, D2, D3, D4] :
    for i, x in enumerate(d) :
        if i < 0 : d[i] = [0]*len(x)

print(D2[1])

plt.figure()
plt.subplot(4, 1, 1)

librosa.display.specshow(librosa.amplitude_to_db(D1, ref=np.max, ), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 2)

librosa.display.specshow(librosa.amplitude_to_db(D2, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 3)

librosa.display.specshow(librosa.amplitude_to_db(D3, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 4)

librosa.display.specshow(librosa.amplitude_to_db(D4, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')


y1, sr1 = librosa.load("ill1s1.mp3")
D1 = librosa.stft(y1, hop_length=128)
y2, sr2 = librosa.load("ill1s2.mp3")
D2 = librosa.stft(y2, hop_length=128)

y3, sr3 = librosa.load("ill1s3.mp3")
D3 = librosa.stft(y3, hop_length=128)
y4, sr4 = librosa.load("ill1s4.mp3")
D4 = librosa.stft(y4, hop_length=128)

for d in [D1, D2, D3, D4] :
    for i, x in enumerate(d) :
        if i < 0 : d[i] = [0]*len(x)

print(D2[1])

plt.figure()
plt.subplot(4, 1, 1)

librosa.display.specshow(librosa.amplitude_to_db(D1, ref=np.max, ), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 2)

librosa.display.specshow(librosa.amplitude_to_db(D2, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 3)

librosa.display.specshow(librosa.amplitude_to_db(D3, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.subplot(4, 1, 4)

librosa.display.specshow(librosa.amplitude_to_db(D4, ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Full power spectrogram')

plt.show()
