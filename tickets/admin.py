from django.contrib import admin
from .models import Bug


class BugAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'updated_date', 'author', 'status')
    list_filter = ['published_date', 'status']
    search_fields = ['title', 'text']

admin.site.register(Bug, BugAdmin)
# Register your models here.
