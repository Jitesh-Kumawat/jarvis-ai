
import requests

def weather():
    API_KEY = "cd4ee863356f01ec78589d282606fba3"
    city = "Kota"  # Replace with your city if needed
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"{temp}°C, {desc}"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"