import speech_recognition as sr
import pyttsx3
import wikipedia


listner=sr.Recognizer()
player = pyttsx3.init()

def listen():
    with sr.Microphone() as input_device:

        print("I am ready, Listening ....")
        voice_content=listner.listen(input_device)
        text_command = listner.recognize_google(voice_content)
        print(text_command)

    return text_command

def talk(text):
    player.say(text)
    player.runAndWait()


def run_voice_bot():
    command = listen()
    if "What is" in command:
        command = command.replace("What is")
        info = wikipedia.summary(command,5)
        talk(info)



run_voice_bot()

