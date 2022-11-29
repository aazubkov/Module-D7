from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username.title()}'


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name.title()}'


class Post(models.Model):
    NEWS, ARTICLE = 'N', 'A'
    TYPES = [(NEWS, 'Новость'), (ARTICLE, 'Статья')]
    type = models.CharField(max_length=1, choices=TYPES, default=NEWS)
    title = models.CharField(max_length=255, unique=True)
    posted = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('post_id_view', args=[str(self.id)])