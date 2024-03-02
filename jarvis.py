import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
print(voices[1].id)

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning")
    elif(hour<=12 and hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
    speak("I am Jarvis Sir. Please Tell me how may I help you?")

def takeCommand():
    '''
    It takes microphone input from the user and return the string output
    '''
    r = sr.Recognizer() #help to recognize the audio of the user
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizeing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User said: {query} \n")
        
    except Exception as e:
        # print(e)
        print("Say that again please ...")
        return "None"
    return query
            
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('photoarrange3@gmail.com','photoarrange123')
    server.sendmail('rathoregaurav275@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower() 
    #Logic for Excecution tasks based on query
    
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("Wikipedia" , "")
        result = wikipedia.summary(query,sentences=2)
        speak("According to WikiPedia")
        print(result)
        speak(result)    

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        
    elif 'open google' in query:
        webbrowser.open("google.com")
        
    elif 'open StackOverFlow' in query:
        webbrowser.open("stackoverflow.com") 
    
    elif 'play music' in query:
        music_dir = "C:\\Users\\ratho\\Music"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,random.choice(songs)))
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    
    elif 'open code' in query : 
        codepath = "C:\\Users\\ratho\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    
    elif 'send email' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "photoarrange3@gmail.com"
            sendEmail(to,content)
            speak("Email has been Sent!")
        except Exception as e:
            print(e)
            speak("Sorry my friend Gaurav . I am not able to send email")
            