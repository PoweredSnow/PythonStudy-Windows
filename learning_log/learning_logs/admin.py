from django.contrib import admin

# Register your models here.
from .models import Entry, Topic

admin.site.register(Topic)
admin.site.register(Entry)
