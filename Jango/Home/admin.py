from django.contrib import admin, messages
from .models import Article, Person

# Register your models here.

@admin.action(description="نمایش دادن مقالات انتخاب شده")
def make_article_published(self, request, queryset):
     queryset.update(is_show=True)
     self.message_user(request, "مقالات انتخاب شده با موفقیت به نمایش در امدند", messages.SUCCESS)

@admin.action(description="پنهان کردن مقالات انتخاب شده")
def make_article_unpublished(self, request, queryset):
    queryset.update(is_show=False)
    self.message_user(request, "مقالات انتخاب شده با موفقیت پنهان شدند", messages.SUCCESS)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'auther', 'pub_date', 'is_show')
    search_fields = ['title', 'pub_date']
    list_filter = ['pub_date']
    list_editable = ['is_show']
    ordering = ['title']
    actions = [make_article_published, make_article_unpublished]
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
    list_display = ('first_name', 'last_name', 'email', 'age')
    search_fields = ('first_name', 'last_name')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)


