# import library
import webbrowser
from time import ctime
import os
import playsound
from gtts import gTTS
import random
import datetime
import requests
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


# Reading Audio file as source
# listening the audio file and store in audio_text variable
def Bixby_Speak(audios):
    tts = gTTS(text=audios, lang='ar', slow=False)
    # tts = gTTS(text=audios, lang='en')
    audioF = 'audio.mp3'
    tts.save(audioF)
    playsound.playsound(audioF)
    print(audios)
    os.remove(audioF)


def record(ask=False):
    with sr.Microphone(device_index=None) as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            Bixby_Speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="ar-EG")
        except sr.UnknownValueError:
            Bixby_Speak("مش سامعة كويس")
        except sr.RequestError:
            Bixby_Speak("السيرفر واقع")
        return voice_data.lower()


def Respond(voice_data):
    if 'الاسم' in voice_data or 'اسم' in voice_data:
        Bixby_Speak('اهلا منون')
        # Bixby_Speak('Moatasem Big Boss')
    if 'الوقت' in voice_data or 'الساعه' in voice_data:
        Bixby_Speak(ctime())
    if 'بحث' in voice_data or 'دور' in voice_data:
        search = record('عن ايه')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Bixby_Speak('خلصانه بشياكه')

    if 'المكان' in voice_data or 'فين' in voice_data:
        location = record("اسم المكان")
        # location = record("what is the location do want ")
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        Bixby_Speak('خلصانه بشياكه')
    
    if 'اهلا' in voice_data:
        Bixby_Speak('اهلا وسهلا')
    
    if 'الصلاة' in voice_data or 'مواقيت' in voice_data:
        date_now = datetime.datetime.now()
        response= requests.get("http://api.aladhan.com/v1/calendarByCity/"+str(date_now.year)+"/"+str(date_now.month)+"?city=Cairo&country=Egypt&method=5")
        if response.status_code ==200:
         data=response.json()
         x=data["data"][0]["timings"]
 #        print(x)
         Bixby_Speak(str(x).strip())
         Bixby_Speak('خلصانه بشياكه')


    if 'قفل' in voice_data:
        Bixby_Speak('تصبحوا علي خير')
        exit()


Bixby_Speak('صباح الفل')
while 1:
    voice_data = record()
    Respond(voice_data)
