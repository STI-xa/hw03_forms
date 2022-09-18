from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        'name of group',
        max_length=200,
    )
    slug = models.SlugField('URL address', unique=True)
    description = models.TextField('description of the group')

    def __str__(self):
        return f'{self.title}'


class Post(models.Model):
    text = models.TextField('posts text')
    pub_date = models.DateTimeField('date of post', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='author of the post',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='group of the posts',
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']
