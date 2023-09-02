# Import necessary libraries
import webbrowser                   # For opening web pages in a browser
from time import ctime              # For getting the current time
import os                           # For interacting with the operating system
import playsound                    # For playing audio files
from gtts import gTTS               # For text-to-speech conversion
import random                       # For generating random numbers
import speech_recognition as sr     # For speech recognition


# Initialize the recognizer class (for recognizing speech)
r = sr.Recognizer()


# Define a function to convert text to speech and play it
def Bixby_Speak(audios):
    tts = gTTS(text=audios, lang='en', slow=False)
    audioF = 'audio.mp3'
    tts.save(audioF)
    playsound.playsound(audioF)
    print(audios)
    os.remove(audioF)

# Define a function to record audio and recognize speech
def record(ask=False):
    with sr.Microphone(device_index=None) as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            Bixby_Speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en")
        except sr.UnknownValueError:
            Bixby_Speak("Sorry, I did not get that.")
        except sr.RequestError:
            Bixby_Speak("Sorry, the service is down.")
        return voice_data.lower()

# Define a function to respond to voice commands
def Respond(voice_data):
    if 'hello' in voice_data:
        Bixby_Speak('Welcome, sir.')
        
    if 'who am i' in voice_data:
        Bixby_Speak('You are my boss, Youssef.')

    if 'time' in voice_data or 'hour' in voice_data:
        Bixby_Speak(ctime())

    if 'search' in voice_data or 'the search' in voice_data:
        search = record('Search initiated. Please wait.')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Bixby_Speak('Search done for ' + search)

    if 'place' in voice_data or 'where' in voice_data:
        location = record("Hello from the location.")
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        Bixby_Speak('Location done for ' + location)

    if 'exit' in voice_data:
        exit()

# Greet the user
Bixby_Speak('Good morning.')

# Main loop for listening to voice commands
while 1:
    voice_data = record()
    Respond(voice_data)
