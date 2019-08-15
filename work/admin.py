from django.contrib import admin

from .models import Projects, Contacts, Analytics, PageData

admin.site.register(Projects)
admin.site.register(Contacts)
admin.site.register(Analytics)
admin.site.register(PageData)
