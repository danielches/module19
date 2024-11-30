from django.contrib import admin
from django.urls import path
from task1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/', home_view),
    path('platform/games/', games_view),
    path('platform/cart/', cart_view),
    path('sign_up/', sign_up)
]