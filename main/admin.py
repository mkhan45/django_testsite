from django.contrib import admin
from .models import Article
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/Date", {"fields": ["article_title", "article_date"]}),
        ("Content", {"fields":["article_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Article, ArticleAdmin)
