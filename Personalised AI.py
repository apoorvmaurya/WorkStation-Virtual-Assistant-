import pyttsx3 
import speech_recognition as sr 
import requests
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your WorkStation Sir. How may I help you")       


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Sorry Sir, I didn't get that. Please say that again")   
        print("Say that again please...")  
        return "None"
    return query

def getRandomJoke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke = response.json()
    if 'setup' in joke and 'punchline' in joke:
        return joke['setup'], joke['punchline']
    else:
        return None, None


if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry! I couldn't find a Wikipedia page for that.")
                query = takeCommand().lower()
                if query != 'none':
                    continue
                else:
                    speak("Invalid search query. Please try again.")

        elif 'my profile' in query:
            speak("Openning your profile Sir!")
            webbrowser.open("linktr.ee/ap00rv")
            
            
        elif 'open youtube' in query:
            speak("Openning Youtube for you Sir!")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Openning Google for you Sir!")
            webbrowser.open("google.com")
        
        elif 'search on google' in query:
            speak("What would you like to search?")
            searchQuery = takeCommand().lower()
            if searchQuery != 'none':
                webbrowser.open(f"https://www.google.com/search?q={searchQuery}")
            else:
                speak("Invalid search query. Please try again.")

        elif 'tell me a joke' in query:
            setup, punchline = getRandomJoke()
            if setup and punchline:
                print(setup)
                speak(setup)
                print(punchline)
                speak(punchline)
            else:
                speak("Sorry, I couldn't fetch a joke at the moment. Please try again later.")


        elif 'open stack overflow' in query:
            speak("Openning Stackoverflow for you Sir!")
            webbrowser.open("stackoverflow.com")   

        elif 'the date' in query:
            currentDate = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Sir, today's date is {currentDate}")

        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open spotify' in query:
            codePath = "C:\\Users\\apoor\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
            os.startfile(codePath)
    
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye, Sir! It was a pleasure serving you.")
            break
