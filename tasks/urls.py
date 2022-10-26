from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('tasks/', admin.site.urls),
]
