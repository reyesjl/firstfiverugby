from django.db import models
from account.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
