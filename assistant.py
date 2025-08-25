# importing require modules
import os
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser

# create engine for text to speech
engine = pyttsx3.init()
engine.setProperty("rate",175)

# speak function
def speak(text):
    print("Assistance:",text)
    engine.say(text)
    engine.runAndWait()

# talking command
def take_command()-> str:
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            command = command.lower()
            print("you said:", command)
            return command
        except:
            return ""

# run assistant
def run_assistant():
    command = take_command()
    # if command has time word
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %P")
        speak(f"The correct time {time}")

    elif'open notepad' in command:
        speak("Opening notepad")
        os.system('notepad')
    
    # open youtube
    elif 'open youtube' in command:
        speak("Opening youtube")
        webbrowser.open("https://youtube.com")
    
    # search in google any query
    elif 'hey siri' in command:
        query = command.replace("hey siri", "").strip()
        if query:
           url = f"https://www.google.com/search?q={query}"
           speak(f"searching for {query}")
           webbrowser.open(url)
        else:
            speak("I am here to assist you")
    # stop assistant
    elif 'bye' in command or 'stop' in command:
        speak("okay, see you again")
        exit()
    else:
        speak("if you need help ping me")

# main function
if __name__=="__main__":
    speak("Hello Manohar, if you need help ping me")
    while True:
        run_assistant()
