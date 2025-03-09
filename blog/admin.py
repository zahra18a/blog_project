from django.contrib import admin
from django.utils.text import Truncator

from . import models

class FilterByTitle(admin.SimpleListFilter):
    title = 'بر اساس کلید های پر تکرار'
    parameter_name = 'title'
    def lookups(self, request, model_admin):
        return (
            ('django', 'جنگو'),
            ('python','پایتون')
        )
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_body', 'author', 'show_image')
    list_display_links = ('short_body',)
    list_editable = ('title',)
    list_filter = ('pub_date','created',FilterByTitle)
    search_fields = ('title','body')
    fields = ('image','title', 'body')

    def short_body(self, obj):
        return Truncator(obj.body).chars(50)

    short_body.short_description = "خلاصه متن"

# admin.site.register(models.Article)
admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)