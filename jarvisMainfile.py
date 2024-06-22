import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, Qt
from jarvisMainGUI import Ui_Form

# start the import part for jia
import pyttsx3      # pip install pyttsx3
import datetime     
import speech_recognition as sr     #pip install SpeechRecognition
import wikipedia        #pip install wikipedia
import webbrowser       #pip install webbrowser
import os
import pyautogui        #pip install pyautogui
import pyjokes          #pip install pyjokes
                        #pip install setuptools

from time import sleep
from datetime import timedelta
# from datetime import datetime
import pywhatkit        #pip install pywhatkit

from pynput.keyboard import Key,Controller  #pip install pynput

import speedtest

import random


import wolframalpha #pip install wolframalpha

import json

import requests
from bs4 import BeautifulSoup



# ===========================================================start the Jia Code====================================================================
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    ui.updateMoviesDynamically("speaking")
    engine.say(audio)
    engine.runAndWait()

def wishings():
    ui.updateMoviesDynamically("speaking")
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")

    speak("Please tell me, How can I help you ?")

# ****************start whatsApp part***************************

strTime = int(datetime.datetime.now().strftime("%H"))
update = int((datetime.datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you wan to message")
    a = int(input('''Person 1 - 1
    Person 2 - 2'''))
    if a == 1:
        speak("Whats the message")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+918626086403",message,time_hour=strTime,time_min=update) #Enter The number here instead of +91000
    elif a==2:
        pass

# ****************end whatsApp part*****************************


# ****************start keyboard part*****************************

keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


# ****************end keyboard part*****************************


# ****************start system part*****************************

dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
        
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")



# ****************end system part*****************************


# ****************start searchNow part*****************************
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what i found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        Results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(Results)
        speak(Results) 


# ****************end searchNow part*****************************

# ****************start News part*****************************

def latestnews():
    api_dict = {"business" :"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=6d09e21c2a1b405a94442b260a36c966" ,#Enter Your OWN API ,
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=6d09e21c2a1b405a94442b260a36c966",#Enter Your OWN API ,
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=6d09e21c2a1b405a94442b260a36c966",#Enter Your OWN API,
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=6d09e21c2a1b405a94442b260a36c966",#Enter Your OWN API,
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=6d09e21c2a1b405a94442b260a36c966",#Enter Your OWN API,
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=6d09e21c2a1b405a94442b260a36c966"#Enter Your OWN API
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            ui.terminalPrint(url)
            ui.terminalPrint("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        ui.terminalPrint(article)
        speak(article)
        news_url = articles["url"]
        ui.terminalPrint(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")

# ****************end news part*****************************


# ****************start calculation part*****************************
def WolfRamAlpha(query):
    apikey = "LR33QE-LUP5Q99YK4"   #Enter Your OWN API KEY
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        ui.terminalPrint(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")

# ****************end calculation part*****************************
    

# -------------------------------------------------------------------------------------------------------------------------------------------------

class jarvisMain(QThread):
    def __init__(self):
        super(jarvisMain, self).__init__()

    def run(self):
        self.runJarvis()


    # * BEFORE RUNNING THE CODE MAKE SURE YOU HAVE INTERNET CONNECTION *
    def commands(self):
        ui.updateMoviesDynamically("listening")
        r=sr.Recognizer()
        with sr.Microphone() as source:
            ui.terminalPrint("Listening...")
            r.pause_threshold=1
            r.adjust_for_ambient_noise(source, duration=1)
            audio=r.listen(source)

        try:
            ui.updateMoviesDynamically("loading")
            ui.terminalPrint("Wait for few Moments..")
            query=r.recognize_google(audio,language='en-in')
            ui.terminalPrint(f"You just said: {query}\n")

        except Exception as e:
            ui.terminalPrint(str(e))
            speak("Please tell me again")
            query="none"
        return query

    def wakeUpCommands(self):
        ui.updateMoviesDynamically("sleeping")
        r=sr.Recognizer()
        with sr.Microphone() as source:
            
            ui.terminalPrint("Jarvis is Sleeping...")
            r.pause_threshold=1
            r.adjust_for_ambient_noise(source,duration=1)
            audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in')
            ui.terminalPrint(f"User said: {query}\n")
        except Exception as e:
            query="none"
        return query

# ------------------------------------------------------------------------------------------------------------------------------------------------------

    #  if __name__ == "__main__":          # Before running the code make sure you have Internet Connection 
    
    def runJarvis(self):
        while True:
            query=self.wakeUpCommands().lower()
            if "hello" in query:
                import pyautogui #pip install pyautogui
                wishings()
                # speak("Yes BOSS What can I do for you!")
                while True:
                    
                    query=self.commands().lower()
                    if "wikipedia" in query:
                        speak("Searching in Wikipedia")
                        try:
                            query=query.replace("wikipedia","")
                            results=wikipedia.summary(query,sentences=1)
                            speak("According to Wikipedia,")
                            ui.terminalPrint(results)
                            speak(results)
                        except:
                            speak("No Results found Sir...")
                            ui.terminalPrint("No results Found")

                    # .........................................WhatsApp.....................................
                    elif "whatsapp" in query:
                        sendMessage()

                    
                    # .........................................keyboard.....................................

                    elif "volume up" in query:
                        speak("Turning volume up,sir")
                        volumeup()

                    elif "volume down" in query:
                        speak("Turning volume down, sir")
                        volumedown()

                    
                    # .........................................easy to open anything.....................................
                    elif "open" in query:   #EASY METHOD
                        query = query.replace("open","")
                        query = query.replace("jiya","")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")   

                    
                    # .........................................Internet Speed.....................................
                    elif "internet speed" in query:
                        wifi = speedtest.Speedtest()
                        wifi.get_best_server()
                        upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
                        download_net = wifi.download() / 1048576
                        ui.terminalPrint(f"Wifi Upload Speed is {upload_net} megabits per second")
                        ui.terminalPrint(f"Wifi download speed is {download_net} megabits per second")
                        speak(f"Wifi download speed is {download_net} megabits per second")
                        speak(f"Wifi Upload speed is {upload_net} megabits per second")


                    # .........................................Screenshot.....................................
                    elif "screenshot" in query:
                        import pyautogui #pip install pyautogui
                        im = pyautogui.screenshot()
                        im.save("ss.jpg")
                        ui.terminalPrint(f"screenshot taken sucessfully")
                        speak(f"screenshot taken sucessfully")

                    
                    # .........................................click photo.....................................
                    elif "click my photo" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")

                    
                    # .........................................talking  to jia.....................................
                    elif "hello" in query:
                        speak("Hello sir, how are you ?")
                    elif "i am fine" in query:
                        speak("that's great, sir")
                    elif "how are you" in query:
                        speak("Perfect, sir")
                    elif "thank you" in query:
                        speak("you are welcome, sir")

                    
                    # .........................................olaying favorite song on youtube.....................................
                    elif "tired" in query:
                        speak("Playing your favourite songs, sir")
                        a = (1,2,3)
                        b = random.choice(a)
                        c = random.choice(a)
                        d = random.choice(a)
                        if b==1:
                            webbrowser.open("https://www.youtube.com/watch?v=68sN4UMYW50")
                        elif c==2:
                            webbrowser.open("https://www.youtube.com/watch?v=68sN4UMYW50")
                        elif d==3:
                            webbrowser.open("https://www.youtube.com/watch?v=68sN4UMYW50")
                        

                    elif "pause" in query:
                        pyautogui.press("k")
                        speak("video paused")
                    elif "play" in query:
                        pyautogui.press("k")
                        speak("video played")
                    elif "mute" in query:
                        pyautogui.press("m")
                        speak("video muted")
                    
                    # .........................................system part.....................................
                    elif "open" in query:
                        openappweb(query)
                    elif "close" in query:
                        closeappweb(query)

                    # .........................................search Now Part....................................
                    elif "google" in query:
                        searchGoogle(query)
                    elif "youtube" in query:
                        searchYoutube(query)
                    elif "wikipedia" in query:
                        searchWikipedia(query)

                    # .........................................News Part....................................
                    elif "news" in query:
                        latestnews()

                    # .........................................Calculator Part....................................
                    elif "calculate" in query:
                        query = query.replace("calculate","")
                        query = query.replace("jiya","")
                        Calc(query)


                    # .........................................tempracture Part....................................
                    elif "temperature in mumbai" in query:
                        from bs4 import BeautifulSoup
                        import requests
                        search = "temperature in Mumbai"
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        ui.terminalPrint(f"current {search} is {temp}")
                        speak(f"current {search} is {temp}")
                    elif "temperature in gujarat" in query:
                        from bs4 import BeautifulSoup
                        import requests
                        search = "temperature in gujarat"
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        ui.terminalPrint(f"current {search} is {temp}")
                        speak(f"current{search} is {temp}")


                    # .........................................Cricket Part....................................
                    elif "cricket score" in query:
                        from plyer import notification  #pip install plyer
                        import requests #pip install requests
                        from bs4 import BeautifulSoup #pip install bs4
                        
                        url = "https://www.cricbuzz.com/cricket-match/live-scores/"
                        page = requests.get(url)
                        soup = BeautifulSoup(page.text, "html.parser")
                        
                        # Check if the list is not empty before accessing its elements
                        team_elements = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")
                        if team_elements:
                            team1 = team_elements[0].get_text()
                            team2 = team_elements[1].get_text()
                            
                            # Check if there are enough elements in the list before accessing them
                            score_elements = soup.find_all(class_ = "cb-ovr-flo")
                            if len(score_elements) >= 11:
                                team1_score = score_elements[8].get_text()
                                team2_score = score_elements[10].get_text()
                            
                                notification.notify(
                                    title = "IPL SCORE :- ",
                                    message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                                    timeout = 15
                                )
                        else:
                            ui.terminalPrint("No team information found.")

                    elif "shutdown system" in query:
                        speak("Are You sure you want to shutdown")
                        shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                        if shutdown == "yes":
                            os.system("shutdown /s /t 1")

                        elif shutdown == "no":
                            break

                    

                    #########################################################################################3
                    # elif "open youtube" in query:
                    #     speak("opening Youtube")
                    #     webbrowser.open("youtube.com")

                    elif 'time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                        speak(f"Sir, the time is {strTime}")

                    elif "sleep" in query:
                        speak("I'm sleeping Sir...")
                        break
                    elif 'exit program' in query or 'exit the program' in query:
                        speak("I'm Leaving Sir, Byeee...")
                        quit()
                    
                    # elif "open google" in query:
                    #     speak("Opening Google Chrome Sir")
                    #     os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\chrome.exe")        # Use the path of your file here
                    #     while True:
                    #         chromeQuery=self.commands().lower()
                    #         if "search" in chromeQuery:
                    #             youtubeQuery=chromeQuery
                    #             youtubeQuery=youtubeQuery.replace("search","")
                    #             pyautogui.write(youtubeQuery)
                    #             pyautogui.press('enter')
                    #             speak('Searching...')
                                
                    #         elif "close chrome" in chromeQuery or "exit chrome" in chromeQuery or "exit google" in chromeQuery or "close window" in chromeQuery or "close this window" in chromeQuery:
                    #             pyautogui.hotkey('ctrl','w')
                    #             speak("Closing Google Chrome Sir...")
                    #             break
                    
                    elif "magic sentence" in query:
                        speak('Yes Sir, for your Pleasure!')
                        speak('hii, sir how are you ')

                    elif "what can you do for me" in query:
                        speak('Yes sir, Nice Question')
                        speak('As per my Program, I\'m a bot which can perform tasks through your voice commands')

                    elif "cool" in query or "nice" in query or "awsome" in query or "thank you" in query:
                        speak("Yes sir, That's my Pleasure!")

                    elif "minimize" in query or 'minimise' in query:
                        speak('Minimizing Sir')
                        pyautogui.hotkey('win', 'down','down')

                    elif "maximize" in query or 'maximise' in query:
                        speak('Maximizing Sir')
                        pyautogui.hotkey('win', 'up','up')

                    elif "close the window" in query or 'close the application' in query:
                        speak('Closing Sir')
                        pyautogui.hotkey('ctrl','w')

                    # elif "screenshot" in query:
                    #     speak("Taking Screenshot sir...")
                    #     pyautogui.press('prtsc')
                    # elif "open paint" in query:
                    #     speak("Opening Paint Application Sir...")           
                    #     os.startfile('C:\\Windows\\System32\\mspaint.exe')      # Use the path of your file here
                    #     while True:
                    #         paintQuery=self.commands().lower()
                    #         if "close" in paintQuery:
                    #             speak("Closing The Application sir")
                    #             pyautogui.leftClick(x=1344, y=11)
                    #             break
                    #         elif "paste" in paintQuery:
                    #             pyautogui.hotkey('ctrl', 'v')
                    #             speak("Done Sir!")
                    #         elif "save" in paintQuery:
                    #             pyautogui.hotkey('ctrl','s')
                    #             speak("saving sir!")
                    #         elif "minimize" in paintQuery:
                    #             speak('Minimizing Sir')
                    #             pyautogui.hotkey('win', 'down','down')
                    #             break
                    #         elif "maximize" in paintQuery:
                    #             speak('Maximizing Sir')
                    #             pyautogui.hotkey('win', 'up','up')
                    #         elif "minimise" in paintQuery:
                    #             speak('Minimizing Sir')
                    #             pyautogui.hotkey('win', 'down','down')
                    #         elif "maximise" in paintQuery:
                    #             speak('Maximizing Sir')
                    #             pyautogui.hotkey('win', 'up','up')

                    elif "start notepad" in query:
                        speak("Opening Notepad Application sir...")
                        os.startfile('C:\\Windows\\System32\\notepad.exe')          # Use the path of your file here
                        while True:
                            notepadQuery=self.commands().lower()
                            if "paste" in notepadQuery:
                                pyautogui.hotkey('ctrl','v')
                                speak("Done Sir!")
                            elif "save this file" in notepadQuery:
                                pyautogui.hotkey('ctrl','s')
                                speak("Sir, Please Specify a name for this file")
                                notepadSavingQuery=self.commands()
                                pyautogui.write(notepadSavingQuery)
                                pyautogui.press('enter')
                            elif 'type' in notepadQuery:
                                speak("Please Tell me what should I Write...")
                                while True:
                                    writeInNotepad=self.commands()
                                    if writeInNotepad == 'exit typing':
                                        speak("Done Sir.")
                                        break
                                    else:
                                        pyautogui.write(writeInNotepad)
                                    
                            elif "exit notepad" in notepadQuery or 'close notepad' in notepadQuery:
                                speak('quiting Notepad Sir...')
                                pyautogui.hotkey('ctrl', 'w')
                                break
                    elif 'play song' in query or 'sing a song' in query or 'play a song' in query or 'play music' in query or 'play a music' in query:
                        speak("Yes Sir Please Wait a moment")
                        songs=os.listdir('Music')       # Use the path of your file here
                        os.startfile(os.path.join('Musics',songs[0]))        # Use the path of your file here

                    elif 'pause' in query or 'pass' in query:
                        pyautogui.press('space')
                        speak('Done Sir')

                    elif 'joke' in query:
                        jarvisJoke = pyjokes.get_joke()
                        ui.terminalPrint(jarvisJoke)
                        speak(jarvisJoke)

# ===========================================================End the Jia Code====================================================================


startExecution = jarvisMain()

class guiOfJarvis(QWidget):
    def __init__(self):
        super(guiOfJarvis,self).__init__()
        self.jarvisUi = Ui_Form()
        self.jarvisUi.setupUi(self)
        self.runAllMovies()

        self.jarvisUi.exitButton.clicked.connect(self.close)
        self.jarvisUi.enterButton.clicked.connect(self.manualCOdeFromTerminal)

    def runAllMovies(self):
        self.jarvisUi.codingMovie =  QtGui.QMovie("E:/Jia/GUI files/B.G_Template_1.gif")
        self.jarvisUi.codingLabel.setMovie(self.jarvisUi.codingMovie)
        self.jarvisUi.codingMovie.start()

        self.jarvisUi.listeningMovie =  QtGui.QMovie("E:/Jia/GUI files/listening.gif")
        self.jarvisUi.listeningLabel.setMovie(self.jarvisUi.listeningMovie)
        self.jarvisUi.listeningMovie.start()

        self.jarvisUi.speakingMovie =  QtGui.QMovie("E:/Jia/GUI files/speaking.gif")
        self.jarvisUi.jarvisSpeakingLabel.setMovie(self.jarvisUi.speakingMovie)
        self.jarvisUi.speakingMovie.start()

        self.jarvisUi.arcMovie =  QtGui.QMovie("E:/Jia/GUI files/techcircle.gif")
        self.jarvisUi.arcLabel.setMovie(self.jarvisUi.arcMovie)
        self.jarvisUi.arcMovie.start()

        self.jarvisUi.loadingMovie =  QtGui.QMovie("E:/Jia/GUI files/tech loading-cropped.gif")
        self.jarvisUi.loadingLabel.setMovie(self.jarvisUi.loadingMovie)
        self.jarvisUi.loadingMovie.start()

        self.jarvisUi.backgroundMovie =  QtGui.QMovie("E:/Jia/GUI files/background.gif")
        self.jarvisUi.backgroundLabel.setMovie(self.jarvisUi.backgroundMovie)
        self.jarvisUi.backgroundMovie.start()

        self.jarvisUi.sleepingMovie =  QtGui.QMovie("E:/Jia/GUI files/sleepmode.gif")
        self.jarvisUi.sleepingLabel.setMovie(self.jarvisUi.sleepingMovie)
        self.jarvisUi.sleepingMovie.start()

        startExecution.start()

    def updateMoviesDynamically(self, state):
        if state == "listening":
            self.jarvisUi.listeningLabel.raise_()
            self.jarvisUi.jarvisSpeakingLabel.hide()
            self.jarvisUi.loadingLabel.hide()
            self.jarvisUi.sleepingLabel.hide()
            self.jarvisUi.listeningLabel.show()

        elif state == "speaking":
            self.jarvisUi.jarvisSpeakingLabel.raise_()
            self.jarvisUi.listeningLabel.hide()
            self.jarvisUi.loadingLabel.hide()
            self.jarvisUi.sleepingLabel.hide()
            self.jarvisUi.jarvisSpeakingLabel.show()

        elif state == "loading":
            self.jarvisUi.loadingLabel.raise_()
            self.jarvisUi.listeningLabel.hide()
            self.jarvisUi.jarvisSpeakingLabel.hide()
            self.jarvisUi.sleepingLabel.hide()
            self.jarvisUi.loadingLabel.show()
        
        elif state == "sleeping":
            self.jarvisUi.sleepingLabel.raise_()
            self.jarvisUi.listeningLabel.hide()
            self.jarvisUi.loadingLabel.hide()
            self.jarvisUi.jarvisSpeakingLabel.hide()
            self.jarvisUi.sleepingLabel.show()

    def terminalPrint(self, text):
        self.jarvisUi.terminalOutputBox.appendPlainText(text)
        # if isinstance(text, str):  # Check if text is a string
        #     self.jarvisUi.terminalOutputBox.appendPlainText(text)
        # else:
        #     print("Error: terminalPrint received a non-string argument.")
    

    def manualCOdeFromTerminal(self):
        cmd = self.jarvisUi.terminalInputBox.text()
        if cmd:
            self.jarvisUi.terminalInputBox.clear()
            self.jarvisUi.terminalOutputBox.appendPlainText(f"You Just Typed >> {cmd}")

            if cmd == 'exit':
                ui.close()

            elif cmd == 'help':
                self.terminalPrint("i can perform various tasks")

            else:
                pass
        
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = guiOfJarvis()
    ui.show()
    sys.exit(app.exec_())