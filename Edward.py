
import datetime
import json
import os
import smtplib
import subprocess
import tkinter as tk
import webbrowser
from functools import partial
from urllib.request import urlopen
from random import *

import time
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia as wikipedia
import winshell as winshell
import wolframalpha as wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


assname = 'Edward'

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir !")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    speak("I am your Assistant edward, can't make food but can do a lot of things!")

def time_now():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")

url_joke = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"


def Joke():
    response = requests.get(url_joke)
    json_data = json.loads(response.text)
    joke = json_data["joke"]
    speak("Here's a joke")
    # time.sleep(1)
    speak(joke)

def query_says(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query or "play song" in query:
        speak("Here you go with music")
        webbrowser.open("open.spotify.com")

    elif 'coding time' in query or 'open vs code' in query or 'open visual studio code' in query:
        speak("Here you go Sir")
        os.startfile("C:\\Users\\ATIK SHAIKH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code")

    elif 'the time' in query:
        time_now()


    elif 'send an email' in query:
        try:
            speak("What should I say?")
            content = takeCommand(0)
            speak("whom should i send")
            to = input('To: ')
            sendEmail(to, content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

    elif 'send a mail' in query:
        try:
            speak("What should I say?")
            content = takeCommand(0)
            speak("whom should i send")
            to = input('To: ')
            sendEmail(to, content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

    elif 'how are you' in query:
        speak("I am fine, Thank you")
        speak("How are you, Sir")

    elif 'fine' in query or "good" in query:
        speak("It's good to know that your fine")

    elif "change my name to" in query:
        query = query.replace("change my name to", "")
        assname = query

    elif "change name" in query:
        speak("What would you like to call me, Sir ")
        assname = takeCommand(1)
        speak("Thanks for naming me")

    elif "what's your name" in query or "What is your name" in query:
        speak("My friends call me")
        speak(assname)
        print("My friends call me", assname)

    elif 'exit' in query:
        speak("Thanks for giving me your time")

    elif "who made you" in query or "who created you" in query:
        speak("I have been created by you to take over the world")
        speak("Just kidding can't do that with a ryzen 5 processor")

    elif 'joke' in query:
        Joke()

    elif "calculate" in query:

        app_id = "2AQX89-J375LL27TP"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        speak("The answer is " + answer)

    elif 'search' in query:

        query = query.replace("search", "")
        webbrowser.open(query)

    elif "who am i" in query:
        speak("If you talk then definately your human.")

    elif "why did you came to this world" in query:
        speak("Thanks to you. further It's a secret")


    elif 'is love' in query:
        speak("It is 7th sense that destroy all other senses")

    elif "who are you" in query or "your name" in query:
        speak("I am your virtual assistant created by you sir")

    elif 'reason for you' in query:
        speak("I was created as a Minor project by you sir ")


    elif 'news' in query:

        try:
            jsonObj = urlopen(
                '''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=bfe7c9c88f7d4d0dba692c880f993fa6''')
            data = json.load(jsonObj)
            i = 1

            speak('here are some top news from the times of india')
            print('''=============== TIMES OF INDIA ============''' + '\n')

            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:

            print(str(e))


    

    elif 'shutdown system' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif 'empty recycle bin' in query:
        speak("Recycle Bin is being Recycled")
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
            speak("Recycle Bin Recycled")
        except:
            speak("Oops Nothing to recycle")

    elif "don't listen" in query or "stop listening" in query:
        speak("for how much time you want to stop edward from listening commands")
        a = int(takeCommand(0))
        time.sleep(a)
        print(a)

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("User asked to Locate")
        speak(location)
        webbrowser.open("https://www.google.nl/maps/place/"+ location + "")


    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in query or "sleep" in query:
        speak("Hibernating")
        subprocess.call("shutdown /h")

    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        time_now.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif "write a note" in query:
        speak("What should i write, sir")
        note = takeCommand(0)
        file = open('Edward.txt', 'w')
        speak("Sir, Should i include date and time")
        snfm = takeCommand(0)
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
            speak("done")
        else:
            file.write(note)
            speak("done")

    elif "show note" in query:
        speak("Showing Notes")
        file = open("Edward.txt", "r")
        print(file.read())
        speak(file.read(6))

    
    elif "Edward" in query:
        wishMe()
        speak("Edward in your service sir!")
        

    elif "wikipedia" in query:
        webbrowser.open("wikipedia.com")

    elif "Good Morning" in query:
        speak("A warm" + query)
        speak("How are you sir")
        

    # most asked question from google Assistant
    elif "will you be my gf" in query or "will you be my bf" in query:
        speak("I'm not sure about, may be you should give me some time")

    elif "how are you" in query:
        speak("I'm fine, glad you me that")

    elif "i love you" in query:
        speak("Love is complicated to me, and you are out of my league")

    elif "what is" in query or "who is" in query:

        # Use the same API key
        # that we have generated earlier
        client = wolframalpha.Client("2AQX89-J375LL27TP")
        res = client.query(query)
        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            print("No results")
        
    elif 'game' in query:
        speak("Let's play a game!")
        speak("I will select a number between one to 10, you have to guess the number")
        speak("you will get 3 chances and one hint if you ask me for a hint, goodluck!")
        speak("are you ready?")
        try:
            usr_ans = takeCommand(1).lower()
        except:
            speak("pardon")
            usr_ans = takeCommand(1).lower()
        if "yes" in usr_ans:
            actual_number = randint(1, 10)
            speak("guess the number!")
            tries = 3
            hint = 0
            while(tries > 0):
                inp = 0
                guessed_number = takeCommand(1)
                print(guessed_number)
                try:
                    guessed_number = int(guessed_number)    
                    if guessed_number == actual_number:
                        speak("Perfect, You Won")
                        break
                    if guessed_number != actual_number:
                        speak("Wrong!")
                except:
                    guessed_number = guessed_number.lower()
                    if "stop" in guessed_number:
                        speak("Sure")
                        break
                    
                    if "hint" in guessed_number:
                        if hint == 0:
                            rand1 = randint(0, 4)
                            rand2 = randint(6, 10)
                            rand3 = randint(1, 2)
                            if actual_number > 5:
                                spk = "The number is greater than ", rand1 
                                speak(spk)
                            if actual_number < 5:
                                spk = "the number is smaller than ", rand2
                                speak(spk)
                            if actual_number == 5:
                                if rand3 == 1:
                                    spk = "The number is greater than ", rand1
                                    speak(spk)
                                if rand3 == 2:
                                    spk = "the number is smaller than", rand2
                                    speak(spk)
                        if hint == 1:
                            speak("You have used your hint!")
                            inp = 1
                        hint = 1
                    else:
                        inp = 1
                        speak("Only hint, stop or any number are acceptable as input")
                if inp == 1:
                    continue
                if inp == 0:
                    tries = tries - 1
            else:
                speak("You lost!")
        if "no" in usr_ans:
            speak("Ok no problem")

def query_string_to_query(query_string):
    query = query_string.get()
    query_says(query)

def manual_input():
    root = tk.Tk()
    root.title("Personal Assistant")
    root.geometry("400x400")
    query_label = tk.Label(root, text="Enter your query: ", fg="red").grid(row=0, column=0)
    query_string = tk.StringVar()
    query_entry = tk.Entry(root, textvariable=query_string, width=25, bg="pink").grid(row=0, column=1)
    submit_button = tk.Button(root, text="GO", fg="red", command=partial(query_string_to_query, query_string)).grid(row=1, column=1)
    exit_button = tk.Button(root, text="Exit", fg="red",command = root.destroy).grid(row=2, column=1)
    root.mainloop()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand(for_game):
    if for_game == 1:
        r = sr.Recognizer()

        with sr.Microphone() as source:

            speak("listening")
            r.pause_threshold = 1
            audio = r.listen(source)

        
        speak("hold on")
        usr_ans = r.recognize_google(audio, language='en-in')
        print(f"User said: {usr_ans}\n")
        return usr_ans
        
    if for_game == 0:
        r = sr.Recognizer()

        with sr.Microphone() as source:

            speak("listening")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            speak("hold on")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query

        except Exception as e:
            print(e)
            speak("Unable to Recognize your voice, wanna try again? if yes press y if u would like to type your query enter type")
            try_again = input("press y to try again press n to exit enter type to type your query").lower()
            if try_again == 'y':
                takeCommand(0)
            if try_again == 'n':
                return None
            if try_again == 'type':
                manual_input()



def sendEmail(to, content):
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login('atikshaikh436@gmail.com', '9869386618')
    smtpserver.sendmail('atikshaikh436@gmail.com', to, content)  
    smtpserver.quit()
    


wishMe()

while True:
    try:
        query = takeCommand(0).lower()
        query_says(query)
    except:
        speak("What was that?")
        query = takeCommand(0).lower()
        query_says(query)
   


    

    
