"""Django Admin Site configuration for socialprofiles"""

# pylint: disable=R0904

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import TermsAndConditions, UserTermsAndConditions
    
class TermsAndConditionsAdmin(admin.ModelAdmin):
    """Sets up the custom Terms and Conditions admin display"""
    list_display = ('slug', 'name', 'date_active', 'version_number',)

class UserTermsAndConditionsAdmin(admin.ModelAdmin):
    """Sets up the custom User Terms and Conditions admin display"""
    list_display = ('terms', 'user', 'date_accepted', 'ip_address',)
    date_hierarchy = 'date_accepted'
    list_select_related = True

admin.site.register(TermsAndConditions, TermsAndConditionsAdmin)
admin.site.register(UserTermsAndConditions, UserTermsAndConditionsAdmin)