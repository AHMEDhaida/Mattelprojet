from django.contrib import admin

# Register your models here.
from .models import Installation, Direction

admin.site.register(Installation)
admin.site.register(Direction)