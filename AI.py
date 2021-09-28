import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

print(voices)

engine.setProperty('voice',voices[0].id)
#here voices[0].id is the voice we hear
# 0th is male voice
# 1st is female voice 


def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()
    #this is function to speak data and great the user
    


def wishMe():
    #this function which gets time and wishes accordingly
    
    hour = int(datetime.datetime.now().hour)
    #hour is variable which gets time as int

    if hour>=0 and hour<12:
        speak("good morning to you sir !")
        speak("I an an AI to help you created by Daksh and Bhautik")
        #checks hour and wishes

    elif hour>=12 and hour<18:
        speak("good afternoon !")
        speak("I an an AI to help you created by Daksh and Bhautik")
        #checks hour wishes

    else:
        speak("good evening !")
        speak("I an an AI to help you created by Bhautik and Bhautik")
        #checks hour wishes



def takeCommand():
    #function to take our voice command
    
    r=sr.Recognizer()
    #used to recognize our command
    
    with sr.Microphone() as source:
        #sr.Microphone() uses microphone as input so we can speak command
        print("Listeninng.....")
        r.pause_threshold = 1      
        audio = r.listen(source)
        #basically passsing string in audio
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        #rcongnize_google finds out what we asked and stores in query
        #language is en-in
        print(f"usar said:{query}\n")
    
    except Exception as e:
        #if programm didnt understand what we said
        #print(e)
        print("say again...")
        return "None"
    
    return query


if __name__ == "main":
        wishMe()


x=0

while x==0:
    
    query = takeCommand().lower()
    
    if 'wikipedia' in query :
        
        speak('seraching on wiki..')
        query = query.replace("wikipedia","")  
        results = wikipedia.summary(query,sentences=2)
        speak("from wikipedia")
        speak(results)
    
    elif 'open youtube' in query:
        
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        
        webbrowser.open("google.com")
    
    elif 'play music' in query:
        
        music_dir = 'E:\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    
    elif 'time' in query :
        
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(strTime)
    
    elif 'kill' in query:
        x+=1