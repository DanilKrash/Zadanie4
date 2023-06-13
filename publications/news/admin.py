from django.contrib import admin
from news.models import Record, Comment


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'text', 'date', 'hidden', 'logo')
    list_display = ('name', 'date', 'hidden')
    readonly_fields = ('date',)
    list_filter = ('date', 'hidden')
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('author', 'image', 'text', 'date')
    list_display = ('author', 'date')
    readonly_fields = ('date',)
    list_filter = ('date',)
    search_fields = ('author',)