from django.contrib import admin

from .models import *


@admin.register(Files)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'slug', 'file', 'type', 'size', 'kb_size',)
    fields = ['text', 'user', 'file', 'type', 'size', 'kb_size', ]
    autocomplete_fields = ["user"]


admin.site.register(FileTypes)
admin.site.register(TopFileTypes)
