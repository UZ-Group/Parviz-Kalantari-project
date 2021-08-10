from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin change site header
admin.site.site_header = 'پنل مدیریت سایت استاد پرویز کلانتری'

UserAdmin.fieldsets[2][1]['fields'] = (
                                        'is_active', 
                                        'is_staff', 
                                        'is_superuser', 
                                        'is_author',
                                        'receive_email', 
                                        'groups', 
                                        'user_permissions'
                                        )

UserAdmin.list_display += ('is_author','is_active', 'receive_email')

admin.site.register(User, UserAdmin)