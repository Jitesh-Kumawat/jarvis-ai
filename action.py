import text_to_speech
import speech_to_text
import datetime
import webbrowser
import os
import weather

def Action(data):
    user_data=data.lower()
    
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("my name is jarvis ai")
        return "my name is jarvis ai"

    elif "hi" in user_data or "hey" in user_data:
        text_to_speech.text_to_speech("hey, sir how i can help you")
        return "hey, sir how i can help you"

    elif "good morning " in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return "good morning sir"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time.hour)+ "Hour :", (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time
        
    elif "shut down" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"
        
    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is opened for you ")
        return "youtube.com is opened for you "
        
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is opened for you")
        return "google.com is opened for you"
    
    elif "play music" in user_data:
        os.startfile(r"C:\Users\Jitesh Kumawat\Music\song SD card\Dj song\[DB] 02 Yo Yo Honey Singh - Brown Rang.mp3")
        text_to_speech.text_to_speech("music is playing for you    Enjoy your music")
        return "music is playing for you"
    
    
    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
    
    elif "thanks buddy" in user_data:
        text_to_speech.text_to_speech("welcome sir")
        return "welcome sir"
        
    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"
    