from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Instrument

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('instruments',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Instrument)
