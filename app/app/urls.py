from django.contrib import admin
from django.urls import path
from task2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list),
]