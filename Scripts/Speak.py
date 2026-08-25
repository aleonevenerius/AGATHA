import pyttsx3
def AGATHAspeaks():
    a = input('Speak it: ')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') # Getting the property 'voices'
    engine.setProperty('voice', voices[1].id) # Define the voice. In this case is '1 Microsoft Zira Desktop - English (United States)' 
    #engine.say(a)
    engine.say(a)
    #engine.save_to_file(a, 'C:\\Virtual Assistance\\AGATHA\\Sounds\\Speak.mp3') # Saving the speak
    engine.runAndWait()
    # file doesn't encontrado
