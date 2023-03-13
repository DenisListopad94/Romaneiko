from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age')
    list_display_links = ('name',)


admin.site.register(Users, UsersAdmin)


class HobbiesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Hobbies, HobbiesAdmin)


class CafeAdmin(admin.ModelAdmin):
    list_display = ('name', 'adres', 'average_amount')
    list_display_links = ('name', 'adres')


admin.site.register(Cafe, CafeAdmin)


class WorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'pilot_salary')
    list_display_links = ('name', 'pilot_salary')


admin.site.register(Work, WorkAdmin)
