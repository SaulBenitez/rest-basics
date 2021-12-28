from django.contrib import admin
from basic_api.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    readonly_fields = ('date',)

admin.site.register(Article, ArticleAdmin)
