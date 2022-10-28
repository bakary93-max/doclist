from django.contrib import admin

# Register your models here.
from tasks.models import Collection, Tasks

admin.site.register(Collection)
admin.site.register(Tasks)
