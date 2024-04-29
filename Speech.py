import speech_recognition as sr

# obtain audio from the microphone
def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Di algo!")
        audio = r.listen(source)
    return(r.recognize_google(audio,language="es-Fr"))

