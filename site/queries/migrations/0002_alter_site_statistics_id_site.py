# Generated by Django 3.2.16 on 2023-02-12 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_site_description'),
        ('queries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_statistics',
            name='id_site',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.site', verbose_name='id сайта'),
        ),
    ]
