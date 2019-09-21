from django.contrib import admin

from webapp.models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'author_email','status','created_at']
    list_display_links = ['id','author']
    list_filter = ['author', 'status']
    search_fields = ['text', 'author_email']
    fields = ['author', 'author_email', 'text', 'status','created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Record, RecordAdmin)
