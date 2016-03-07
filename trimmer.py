from pylab import *
import pylab
from scipy.io import wavfile

filename = 'AILMENTS SYMPTOMS AND INJURIES II.wav'

sampFreq, snd = wavfile.read(filename)

print('dtype', snd.dtype)
print('sampFreq', sampFreq)
print('shape', snd.shape[0])

print('duracion' ,snd.shape[0]/ sampFreq)

s1 = snd[:,0]

timeArray = arange(0, snd.shape[0], 1)
timeArray = timeArray / sampFreq
timeArray = timeArray  #scale to milliseconds

count = 0
SES = 0
follow = False
lastIndex = 0;
timesTrimmed = 1;

for index, x in enumerate(s1):
    if x < 1000 and x > -1000:
        count = count + 1
        if count > (sampFreq * 0.44):
            if not follow:
                SES = SES + 1
                follow = True
    else:
        if follow:
            #Track Trim Creation
            wavfile.write(filename.replace('.wav', '')+'('+str(timesTrimmed)+')'+'.wav', sampFreq, snd[lastIndex: index - count/2:1])
            timesTrimmed = timesTrimmed + 1
            lastIndex = index - count/2

            count = 0
            follow = False
        else:
            count = 0

wavfile.write(filename.replace('.wav', '')+'('+str(timesTrimmed)+')'+'.wav', sampFreq, snd[lastIndex: snd.shape[0] :1])

print('veces en silencio', SES)

plot(timeArray, s1, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')

pylab.show()
