import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener =sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice =listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('gpprakash0719@gmail.com', '7975545953')
        email =EmailMessage()
        email['From'] = 'gpprakash0719@gmail.com'
        email['To'] = receiver
        email['subject'] = subject
        email.set_content(message)
        server.send_message(email)


email_list = {
    'dad': 'sagayaraja4@gmail.com',
    'mine 1':'ganaprakash0719@gmail.com',
    'mine 2':'gnanaprakash0719@gmail.com'
}

def get_email_info():
    talk('to whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('what s the subject of your email')
    subject = get_info()
    talk('tell me the text in your email')
    message = get_info()
    send_email(receiver , subject ,message)

get_email_info()
