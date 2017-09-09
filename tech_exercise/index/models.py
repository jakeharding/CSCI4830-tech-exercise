from django.db import models as m


class BlogEntry(m.Model):
    title = m.CharField(max_length=256)
    author = m.CharField(max_length=256)
    email = m.EmailField()
    article = m.TextField()
    created_at = m.DateTimeField(auto_now_add=True)
