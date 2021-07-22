from django.shortcuts import render
from .models import SiteSetting

# Create your views here.
def contact_us(request):
    context ={
        'setting' : SiteSetting.objects.first()
    }
    return render(request, 'site_settings/contact_us.html', context)

def biography(request):
    context ={
        'setting' : SiteSetting.objects.first()
    }
    return render(request, 'site_settings/biography.html', context)