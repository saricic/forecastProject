import requests
import json
import os
from django.shortcuts import render
from django.conf import settings


# Function to fetch and update JSON data
def fetch_weather_data():
    url = "https://raw.githubusercontent.com/saricic/Background-Remover/refs/heads/main/weather.json"
    file_path = os.path.join(settings.BASE_DIR, "data", "weather_data.json")

    # Create the data directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            weather_data = response.json()
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(weather_data, file, indent=4)
            print("✅ Weather data successfully updated!")
        else:
            print(f"❌ Failed to fetch JSON data. Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"❌ Error fetching JSON data: {e}")


# Weather list view
def weather_list(request):
    # Fetch JSON data only if the file does not exist (to avoid unnecessary API calls)
    file_path = os.path.join(settings.BASE_DIR, "data", "weather_data.json")

    if not os.path.exists(file_path):
        fetch_weather_data()

    # Get search query from URL
    search_query = request.GET.get('q', '').strip()

    # Load the JSON file
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            weather_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        weather_data = []  # Return an empty list if the file is missing or invalid

    # Filter the data based on the search query
    filtered_data = [item for item in weather_data if
                     search_query.lower() in item["name"].lower()] if search_query else []

    return render(request, "weather_list.html", {"search_query": search_query, "weather_data": filtered_data})
