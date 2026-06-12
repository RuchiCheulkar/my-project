import google.generativeai as genai
import requests

genai.configure(api_key="AQ.Ab8RN")

model = genai.GenerativeModel("gemini-2.5-flash")

def get_weather(city):
    data = requests.get(f"https://wttr.in/{city}?format=j1").json()

    current = data["current_condition"][0]

    return {
        "city": city,
        "temperature": current["temp_C"],
        "description": current["weatherDesc"][0]["value"]
    }

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    city = query.split()[-1]

    weather = get_weather(city)

    prompt = f"""
    User asked: {query}

    Weather data:
    {weather}

    Answer naturally as a weather assistant.
    """

    response = model.generate_content(prompt)

    print("Bot:", response.text)