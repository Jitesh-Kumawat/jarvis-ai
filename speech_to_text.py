import speech_recognition as sr


def speech_to_text():
    r = sr.Recognizer()
   
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=0.5)  # Reduce background noise delay
        print("listening...")
        audio = r.listen(source, timeout=6, phrase_time_limit=3)  # Limit waiting time
        
    try:
        voice_data=""
        voice_data = r.recognize_google(audio)
        
        print(voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError:
        print("RequestError")


