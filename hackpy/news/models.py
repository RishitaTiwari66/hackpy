from django.db import models

# Create your models here.
# news/models.py

from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class News(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = MarkdownxField()
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]

    def formatted_markdown(self):
        return markdownify(self.content)

class Vote(models.Model):
    news = models.ForeignKey(News, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10, choices=[('up', 'Upvote'), ('down', 'Downvote')])
