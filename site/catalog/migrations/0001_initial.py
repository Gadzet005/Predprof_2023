# Generated by Django 3.2.16 on 2023-01-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='без названия', max_length=100, verbose_name='название')),
                ('url', models.URLField(max_length=100, unique=True, verbose_name='url')),
                ('is_on_catalog', models.BooleanField(default=False, verbose_name='в общем каталоге?')),
            ],
            options={
                'verbose_name': 'сайт',
                'verbose_name_plural': 'сайты',
            },
        ),
    ]