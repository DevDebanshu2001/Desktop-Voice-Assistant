
# Desktop Voice Assistant Project


import webbrowser     
import pyttsx3		 
import speech_recognition as sr  
import wikipedia	
import datetime		
import os			
import random		


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
print(voices[0].id)  
engine.setProperty('voice',voices[0].id)    
rate = engine.getProperty('rate')
newrate = 130								
engine.setProperty('rate', newrate)	


def speak(audio):
    engine.say(audio)						
    engine.runAndWait()
def wishMe():
    speak("Welcome, How are you?")
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")					
    elif hour>=12 and hour<18:
        speak("Good Afternoon !!!")				
    elif hour>=18 and hour<22:
        speak("Good Evening !")
    else:
        speak("Sir!! It's beyond 10pm We must Sleep")
    speak("I am Har e .  How may I help You ")
def takeCommand():
    #It takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.non_speaking_duration = 0.6			
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("User Said: "+r.recognize_google(audio))
        i = random.randrange(0,50)
        if i<25:								
            speak("Copy that")
        else:
            speak("Roger that")
    
    except Exception as e:
        #print(e)
        print("Sir I was unable to hear you Please Say again")    
        speak("Sir I was unable to hear you Please Say again")	
        return "None"
        
    return query    
        

# Main program starts       
if __name__ == "__main__":
    
    wishMe()  # function has been called to greet the owner
	   
    while True:     
        query = takeCommand().lower()   
        
        if 'ok bro' or 'bro' in query:   			
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')  		# Surf to Wikipedia
                query = query.replace("wikipedia", "")   
            #print(query)
                results = wikipedia.summary(query, sentences = 2)
                speak("According to Wikipedia")    
                print(results)
                speak(results)      

            elif 'open youtube' in query: 
                speak("Opening YouTube For You.")
                webbrowser.open("https://www.youtube.com/")

            elif 'google' in query:            					# Browse to google Services
                if 'maps' in query:
                    speak("Opening Google Maps For you.")
                    webbrowser.open("https://www.google.co.in/maps/")
                elif 'drive' in query:
                    speak("Opening Google Drive for you.")
                    webbrowser.open("https://drive.google.com/drive/")
                elif 'translate' in query:
                    speak("Opening Google translate for you.")
                    webbrowser.open("https://translate.google.co.in/")
                else:
                    speak("Opening Google for you.")
                    webbrowser.open("https://www.google.co.in/") 

            elif 'i am sad' in query:
                songs_dir = "D:\\songs"
                songs = os.listdir(songs_dir)							# Play music  for refreshment
                speak("Playing Music for You as refreshment")
                os.startfile(os.path.join(songs_dir, songs[random.randrange(0,14)])) 

            elif 'udemy' in query:
                speak("Opening Udemy for You")
                webbrowser.open("https://www.udemy.com/")

            elif 'pluralsight' in query:
                speak("Opening PluralSight for You.")
                webbrowser.open("https://www.pluralsight.com/")				# Access frequently used web portals

            elif 'coursera' in query:
                speak("Opening Coursera for You.")
                webbrowser.open("https://www.coursera.org/")

            elif 'thank you' in query:
                speak("You are Most Welcome It's my Honor.")            # Thank You  

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is  {strTime}")

            elif 'open dev c' in query:								#  Open System Applications
                codePath = "D:\\Dev-Cpp\\devcpp.exe"
                os.startfile(codePath)

            elif 'open zoom' in query:
                path = "C:\\Users\\rushi\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"  #  Another Example
                os.startfile(path)

            elif 'exit' in query:
                print("Quiting")
                speak("Bye Bye Sir. Hope to see you Soon.")				# Come put of the code
                break
            
        
        
    
   




