import librosa
import librosa.display
import numpy as np
from numpy import linalg as LA
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def analyze(args) : 
    plt.figure()
    for i, pair in enumerate(args):
        data = np.abs(pair[0])

        data = data/LA.norm(data, np.inf)

        for i in data : 
            indexes = i < 0.03
            i[indexes] = 0 

        print(args)

        plt.subplot(len(args), 1, i)
        librosa.display.specshow(librosa.amplitude_to_db(data, ref=np.max), y_axis='log')
        plt.colorbar(format='%+2.0f dB')
        plt.title(pair[1])
    plt.show()