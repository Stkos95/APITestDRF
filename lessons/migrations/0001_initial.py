# Generated by Django 4.2.5 on 2023-10-02 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ViewDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.IntegerField()),
                ('status', models.CharField(choices=[('ПР', 'Просмотрено'), ('НП', 'Не просмотрено')], default='НП', max_length=20)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='products_joined', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='product',
            field=models.ManyToManyField(related_name='lessons', to='lessons.product'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='users',
            field=models.ManyToManyField(through='lessons.ViewDetail', to=settings.AUTH_USER_MODEL),
        ),
    ]
