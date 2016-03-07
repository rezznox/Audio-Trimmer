from pylab import *
import pylab
from scipy.io import wavfile

#replace with the path of the file you want to trim
filename = 'AILMENTS SYMPTOMS AND INJURIES II.wav'

#Number of samples per second and the n-array containing the information in the file
sampFreq, snd = wavfile.read(filename)

print('dtype', snd.dtype)
print('sampFreq', sampFreq)
print('shape', snd.shape[0])

print('duracion' ,snd.shape[0]/ sampFreq)

#Only get 1 channel of sound from the n-array
s1 = snd[:,0]

timeArray = arange(0, snd.shape[0], 1)
timeArray = timeArray / sampFreq
timeArray = timeArray  #scale to milliseconds

#Here starts the trimming process
count = 0
SES = 0
follow = False
lastIndex = 0;
timesTrimmed = 1;

for index, x in enumerate(s1):
    #only trim if the amplitude is below 1000
    if x < 1000 and x > -1000:
        count = count + 1
        #trim when the amplitude has been really low for 0.44 seconds
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
#This if for the rest of the file where sound was found
wavfile.write(filename.replace('.wav', '')+'('+str(timesTrimmed)+')'+'.wav', sampFreq, snd[lastIndex: snd.shape[0] :1])

print('veces en silencio', SES)

#Lets just plot it for the sake of fun

plot(timeArray, s1, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')

pylab.show()

#The code below has much to be improved so don't hesitate to criticize or improve it yourself, both things are cool.
