from django.contrib import admin
from .models import SiteSetting
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'bio', 'contact_us')

admin.site.register(SiteSetting, SettingAdmin)