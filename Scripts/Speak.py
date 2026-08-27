import pyttsx3
def AGATHAspeaks():
    a = "Bottle of water, better, , work, lift"
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') # Getting the property 'voices'
    engine.setProperty('voice', voices[1].id) # Define the voice. In this case is '1 Microsoft Zira Desktop - English (United States)' 
    engine.save_to_file(a, 'C:\\VirtualAssistance\\AGATHA\\Sounds\\Speak.mp3') # Saving the speak
    engine.runAndWait()
