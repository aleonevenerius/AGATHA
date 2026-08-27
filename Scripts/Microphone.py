import sounddevice as sd # Importing the module
import numpy # Import Numpy Library

 
fs = 44100
duration = 4
frames = fs*duration

myarray = sd.rec( # It acess my input device and returns the array.
    frames, 
    samplerate=fs, 
    channels=1
)
sd.wait() # It does Python to wait

sd.play(myarray) # Playing my audio
sd.wait()