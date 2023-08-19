#!/usr/bin/python3
from gtts import gTTS
import vlc
myobj = gTTS(text=' Welcome ahmed ', lang='en', slow=False)
# Saving the converted audio in a mp3 file named
myobj.save("welcome.mp3")
# Playing the converted file
p = vlc.MediaPlayer("./welcome.mp3")
p.play()
while True:
    pass