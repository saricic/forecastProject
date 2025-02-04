import requests
import json
import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

def fetch_weather_data():
    url = "https://raw.githubusercontent.com/saricic/Background-Remover/refs/heads/main/weather.json"
    file_path = os.path.join(settings.BASE_DIR, "data", "weather_data.json")
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

@login_required(login_url='login')
def weather_list(request):
    file_path = os.path.join(settings.BASE_DIR, "data", "weather_data.json")
    if not os.path.exists(file_path):
        fetch_weather_data()

    search_query = request.GET.get('q', '').strip()

    # Load weather data from file
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            weather_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        weather_data = []

    filtered_data = []
    if search_query:
        # Filter the weather data based on the search query
        filtered_data = [
            item for item in weather_data if search_query.lower() in item["name"].lower()
        ]

        # Retrieve the existing search history or initialize it
        search_history = request.session.get('search_history', [])
        # Append the current search as a dictionary with its query and results
        search_history.append({
            'query': search_query,
            'results': filtered_data
        })
        request.session['search_history'] = search_history

    # Always pass the search history (it might be empty)
    search_history = request.session.get('search_history', [])

    return render(request, "weather_list.html", {
        "search_query": search_query,
        "weather_data": filtered_data,
        "search_history": search_history,
    })

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})
