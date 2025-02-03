from django.contrib import admin
from django.urls import path
from weather.views import weather_list, register  # Import the new register view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', weather_list, name='weather_list'),
    path('register/', register, name='register'),  # Registration URL pattern
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
]
