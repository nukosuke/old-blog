from django.db import models

class Entry(models.Model):
    slug         = models.SlugField()
    title        = models.CharField(max_length=255)
    body         = models.TextField()
    created_at   = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=None)
