import json
import os
from django.shortcuts import render
from django.conf import settings

def weather_list(request):
    # Grab the search query from the URL's "q" parameter
    search_query = request.GET.get('q', '')



    ### THINGS TO DO
    # If no search query is provided, we do NOT read the JSON file,
    # so we don't list all cities by default.

