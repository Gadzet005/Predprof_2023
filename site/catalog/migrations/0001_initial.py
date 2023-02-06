# Generated by Django 3.2.16 on 2023-02-05 09:33

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
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('url', models.URLField(max_length=100, verbose_name='url')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/%Y/%m/', verbose_name='логотип')),
                ('description', models.TextField(default='Без описания', max_length=5000, verbose_name='описание')),
                ('is_on_catalog', models.BooleanField(default=False, verbose_name='в общем каталоге?')),
            ],
            options={
                'verbose_name': 'сайт',
                'verbose_name_plural': 'сайты',
            },
        ),
        migrations.CreateModel(
            name='UserSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_site', to='catalog.site', verbose_name='сервис')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_site', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'default_related_name': 'user_site',
            },
        ),
    ]