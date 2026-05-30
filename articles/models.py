from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'