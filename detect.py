import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(name, index)

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print("Say smth.")
    audio = r.listen(source)

query = r.recognize_google(audio, language="ru-RU")
print("you said " + query.lower())