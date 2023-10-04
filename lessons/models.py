from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    owner = models.ForeignKey(User,
                              related_name='products',
                              on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='products_joined')


class Lesson(models.Model):
    product = models.ManyToManyField(Product,
                                     related_name='lessons')

    name = models.CharField(max_length=255)
    url = models.URLField()
    duration = models.IntegerField()
    users = models.ManyToManyField(User, through='ViewDetail')


class ViewDetail(models.Model):
    class Status(models.TextChoices):
        WATCHED = 'Просмотрено'
        UNWATCHED = 'Не просмотрено'

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watched = models.IntegerField()
    status = models.CharField(max_length=20, default=Status.UNWATCHED, choices=Status.choices)
    when_watched = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.watched / self.lesson.duration >= 0.8:
            self.status = self.Status.WATCHED
        super().save(*args, **kwargs)
