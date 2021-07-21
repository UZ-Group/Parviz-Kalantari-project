from django.shortcuts import render
from .models import SiteSetting

# Create your views here.
def contact_us(request):
    context ={
        'setting' : SiteSetting.objects.first()
    }
    return render(request, 'blog/contact_us.html', context)