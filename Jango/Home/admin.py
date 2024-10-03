from django.contrib import admin
from .models import Article, Person
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'auther', 'pub_date', 'is_show')
    search_fields = ['title', 'pub_date']
    list_filter = ['pub_date']
    list_editable = ['is_show']
    ordering = ['title']
    fieldsets = [
        [
            'Article info',
            {'fields': ['title', 'text', 'image', 'is_show'],
             'classes': ['collapse']},
        ],
        [
            'Auther info',
            {'fields': ['auther',]},
        ]
    ]
    raw_id_fields = ['auther']


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)


