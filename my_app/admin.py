from django.contrib import admin
from my_app.models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time',)


admin.site.register(Article, ArticleAdmin)
