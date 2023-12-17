
from django.contrib import admin

from apps.todo.models import Task

# Register your models here.
@admin.register(Task)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created')
    search_fields = ('title', 'description')