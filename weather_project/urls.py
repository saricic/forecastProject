from django.contrib import admin
from django.urls import path
from weather.views import weather_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', weather_list, name='weather_list'),
]
