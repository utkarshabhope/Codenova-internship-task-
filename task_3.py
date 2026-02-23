 import requests

def main():
    city = input("Enter city name: ")

    try:
        # Get coordinates
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_response = requests.get(geo_url, timeout=5)
        geo_data = geo_response.json()

        if "results" not in geo_data:
            print("City not found.")
            return

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        name = geo_data["results"][0]["name"]
        country = geo_data["results"][0]["country"]

        # Get weather
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url, timeout=5)
        weather_data = weather_response.json()

        current = weather_data["current_weather"]

        print("\n====== Weather Report ======")
        print("Location:", name, ",", country)
        print("Temperature:", current["temperature"], "°C")
        print("Wind Speed:", current["windspeed"], "km/h")
        print("============================")

    except requests.exceptions.Timeout:
        print("Request timed out. Check your internet connection.")
    except requests.exceptions.ConnectionError:
        print("Network error. Please check your internet.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()