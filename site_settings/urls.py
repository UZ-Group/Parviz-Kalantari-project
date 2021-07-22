from django.urls import path
from .views import contact_us, biography

app_name = 'setting'
urlpatterns = [
    path('contact-us/', contact_us, name='contact_us'),
    path('biography/', biography, name='biography'),
]