from django.contrib import admin
from django.urls import path
from fkip.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fkip/', index),
]
