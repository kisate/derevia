import librosa
import librosa.display
import numpy as np
import analyzer
import glob

data = []

for i, filename in enumerate(glob.iglob('*.mp3')):
    

    y, sr = librosa.load(filename)
    D = librosa.stft(y, hop_length=128)
    
    data.append((D, filename))

    if i % 4 == 0 : 
        analyzer.analyze(data)
        data = []


    