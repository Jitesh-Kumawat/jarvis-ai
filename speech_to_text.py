# import speech_recognition as sr


# def speech_to_text():
#     r = sr.Recognizer()
   
#     with sr.Microphone() as source:
#         audio = r.listen(source)
        
#     try:
#         voice_data=""
#         voice_data = r.recognize_google(audio)
        
#         print(voice_data)
#         return voice_data
#     except sr.UnknownValueError:
#         print("error")
#     except sr.RequestError:
#         print("RequestError")

# speech_to_text()
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)  # Reduce background noise delay
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=3)  # Limit waiting time
            voice_data = r.recognize_google(audio)
            print("User:", voice_data)
            return voice_data
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            return "Sorry, I didn't understand."
        except sr.RequestError:
            print("Network error.")
            return "Network error."

# Remove speech_to_text() call at the end to avoid auto-execution.
