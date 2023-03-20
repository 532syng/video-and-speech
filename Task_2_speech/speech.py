#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:30:11 2023

@author: syng
"""
# Task 2 Pa Ta Ka

import re
import speech_recognition as sr
from gtts import gTTS

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable
with sr.AudioFile('../ptk_2.wav') as source:    
    audio_text = r.listen(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        r.energy_threshold = 0.00001
        # using google speech recognition
        #text = r.recognize_google(audio_text)   
        results = r.recognize_google(audio_text, language="ko-KR", show_all=True)
        text = results['alternative'][1]['transcript']  # get second alternative
        #'바다가 바다가 바다가 바다가 바다가 바다가'

        print('Converting audio transcripts into text ...')
        print(text)
     
    except:
         print('Sorry.. run again...')
         
        
mytext = text.replace(" ",'')
ind2 = [m.end() for m in re.finditer('바다가', mytext)]

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
#myobj = gTTS(text=mytext, lang='en',  slow=False)

pos=0
with open("ptk_2_out.mp3", 'wb') as f:
    for i in range(len(ind2)):
        phrase = gTTS(text=mytext[pos:ind2[i]], lang='es',  slow=False) 
        number = gTTS(str(i+1), lang='en')
        phrase.write_to_fp(f)
        number.write_to_fp(f)
        pos = ind2[i]
    
  
# Saving the converted audio in a mp3 file named
#myobj.save("ptk_2_out.mp3")
  
