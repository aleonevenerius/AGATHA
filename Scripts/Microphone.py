# Import the module
import sounddevice as sd



print("Recording 3 seconds...")

duration = 3 # seconds
fs = 44100 #
myRecording =  sd.rec(int(duration * fs), samplerate=fs, channels=2)
#sd.play()
sd.wait()

print("Done.")

print("Playing...")

#sd.play(, fs)

print("Done.")