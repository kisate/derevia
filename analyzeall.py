import librosa
import librosa.display
import numpy as np
import analyzer
import glob
from numpy import linalg as LA
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

f = open('za.out', 'w')
def analyze(args) : 
    plt.figure()
    for j, (data, name) in enumerate(args):
        data = np.abs(data)

        f.write(name + "\n")

        for g in range(len(data[0])) : 
            for k in range(len(data)) :
                f.write("{} ".format(str(data[k][g]), name))
            f.write("\n")
        

        #data = data/LA.norm(data, np.inf)

        # for i in data : 
        #     indexes = i < 0.03
        #     i[indexes] = 0 

        # print(args)

        plt.subplot(len(args), 1, j+1)
        # librosa.display.specshow(librosa.amplitude_to_db(data, ref=np.max), y_axis='log')
        # plt.colorbar(format='%+2.0f dB')
        plt.plot(data)
        plt.title(name)
        


data = []

for i, filename in enumerate(glob.iglob('*s?.mp3')):
    

    y, sr = librosa.load(filename)
    D = librosa.stft(y, hop_length=32)
    
    data.append((D, filename))

    if i % 4 == 3 : 
        analyze(data)
        data = []
plt.show()
f.close()