from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_content = models.TextField()
    article_date = models.DateTimeField("Date Published", default=datetime.now())

    def __str__(self):
        return self.article_title
