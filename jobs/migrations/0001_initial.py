# Generated by Django 3.2.9 on 2021-11-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=250)),
                ('tag', models.CharField(max_length=50, verbose_name='Тэг')),
                ('body', models.CharField(max_length=80, verbose_name='Описание')),
                ('user', models.CharField(max_length=20, verbose_name='ник')),
                ('time', models.CharField(max_length=20, verbose_name='время')),
                ('rate', models.CharField(max_length=20, verbose_name='рейтинг')),
                ('hub', models.CharField(max_length=20, verbose_name='хаб')),
                ('suit', models.CharField(max_length=200, verbose_name='сайт')),
                ('date', models.DateField(max_length=50, verbose_name='дата')),
            ],
        ),
    ]