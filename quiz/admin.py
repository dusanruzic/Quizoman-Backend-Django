from django.contrib import admin
from .models import Category, Question, Badge, Player, Statistics
# Register your models here.

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Badge)
admin.site.register(Player)

admin.site.register(Statistics)