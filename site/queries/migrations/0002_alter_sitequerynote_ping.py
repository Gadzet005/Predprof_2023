# Generated by Django 3.2.16 on 2023-02-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitequerynote',
            name='ping',
            field=models.FloatField(verbose_name='задержка мс.'),
        ),
    ]