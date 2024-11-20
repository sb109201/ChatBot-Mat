import pywhatkit
import speech_recognition as sr

import pyttsx3
import datetime
import wikipedia
import pyjokes
import weather
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
   engine.say(text)
   engine.runAndWait()
def take_command():
 try:
     with sr.Microphone() as source:
         print('listening...')
         voice = listener.listen(source)
         command=listener.recognize_google(voice)
         command =command.lower()
         if 'mat' in command:
          command=command.replace('mat','')
          print(command)
 except:
    pass
 return command

def run_mat():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play', '')
        talk('playing' +  song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk('Current time is '+ time)
    elif 'who the heck is' in command:
        person=command.replace('who the heck is' ,' ')
        info=wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        print('sorry,i have a headache')
        talk('sorry,i have a headache')
    elif 'goodbye' in command or 'exit' in command or 'quit' in command:
        talk("Goodbye! Have a great day!")
        exit()
    elif 'how are you' in command:
        talk("I'm just a program, but I'm doing great! How about you?")
    elif 'thank you' in command:
        talk("You're welcome! Happy to help.")
    elif 'are you single' in command:
        print('I am in a relationship With siri')
        talk('I am in a relationship With siri')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please Say the Command again.')
while True:
 run_mat()

