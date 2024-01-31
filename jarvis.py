import pyttsx3
import speech_recognition as sr
# import openai
from openai import OpenAI
import env

# open ai key
client = OpenAI(api_key = env.OPEN_AI_KEY)

# Initialize Speech Engine
engine = pyttsx3.init()

def speak(words):
    engine.setProperty('rate', 135)
    engine.setProperty('volume', 0.8)

    voices = engine.getProperty('voices');
    engine.setProperty('voice', voices[1].id)

    engine.say(str(words))
    engine.runAndWait()
    engine.stop()

# Initialize Speech Recognizer
rec = sr.Recognizer()

speak('Recognizer Initialized, Waiting for your command')

with sr.Microphone() as source:
    audio = rec.listen(source)
    speak('looking answer for your query....')

text = rec.recognize_google(audio)


discussion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": text,
        },
    ],
)

answer = discussion.choices[0].message.content

if answer:
    speak(answer)


