import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import subprocess
import wikipedia
import os


engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<7:
        speak("Good Evening")
    else:
        speak("Hi Sir")
    print("Welcome to Python Assistant. My name is Chappie. How can i help you?")
    speak("Welcome to Python Assistant program. My name is Chappie. How can i help you?")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold =1
        audio=r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing....")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")


    except Exception as e:
        print("say that again")
        speak("i couldn't hear you")
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if "open chrome" in query:
            print("ok sir")
            speak("loading google in chrome")
            os.system("start chrome.exe")
            break

        elif "open youtube" in query:
            print("ok sir")
            speak("loading youtube in chrome")
            webbrowser.open("https://www.youtube.com/")
            break

        elif "open whatsapp web" in query:
            print("ok sir")
            speak("loading whatsapp web in chrome")
            webbrowser.open("https://web.whatsapp.com/")
            break

        elif "open calculator" in query:
            print("ok sir")
            speak("ok sir")
            subprocess.call("calc.exe")
            break

        elif "open notepad" in query:
            print("ok sir")
            speak("ok sir")
            subprocess.call("notepad.exe")
            break

        elif "open CMD" in query:
            print("ok sir")
            speak("ok sir")
            subprocess.call("cmd.exe")
            break


        elif "my computer" in query:
            speak("Opening This PC")
            os.system("start explorer")
            break

        elif"control panel" in query:
            print("ok sir")
            speak("ok sir")
            os.system("start control panel")
            break


        elif "in wikipedia" in query:
            print("searching in wikipedia...")
            query=query.replace("in wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
            break

        elif "open google" in query:
            speak("what do i search in google")
            ssr=takeCommand().lower()
            webbrowser.open(f"{ssr}")
            break

        elif "how are you" in query:
            speak("I am fine. How are you?")


        elif "i am" in query:
            speak("ok sir, How can i help you?")
    

        elif "time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the current time is {time}")
            print(time)


        elif "shutdown" in query:
            speak("Hold On a Second ! System is on its way to shutdown")
            print("Hold On a Second ! System is on its way to shutdown")
            subprocess.call('shutdown / p /f')
        

        elif "restart" in query:
            speak("System is on its way to re-start. Restarting in 1.....2...3")
            subprocess.call(["shutdown","/r"])

        
        elif "visual studio code" in query:
            print("Opening VS Code")
            speak("Here you go to Visual Studio Code. Happy Coding")
            os.system("code")
            break


        elif "open stackoverflow" in query:
            speak("Opening StackOverFlow website for your Problems")
            webbrowser.open("stackoverflow.com")
            break

        elif "your name" in query:
            speak("My name is Chappie. I am here for your help")

        
        elif "turn off" in query:
            speak("Thank you for using me. Have a nice Day")
            exit()

        
        else:
            speak("I did not understand. Please use appropriate command.")