from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')