from django.db import models

# Create your models here.


class Xamerz(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250,)
    tag = models.CharField(max_length=50, verbose_name='Тэг')
    body = models.CharField(max_length=80, verbose_name='Описание')
    user = models.CharField(max_length=20, verbose_name='ник')
    time = models.CharField(max_length=20, verbose_name='время')
    rate = models.CharField(max_length=20, verbose_name='рейтинг')
    hub = models.CharField(max_length=20, verbose_name='хаб')
    suit = models.CharField(max_length=200, verbose_name='сайт')
    date = models.CharField(max_length=50, verbose_name='дата')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Follower(models.Model):
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.email
