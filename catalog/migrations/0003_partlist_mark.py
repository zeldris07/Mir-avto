# Generated by Django 4.0.4 on 2022-05-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_partlist_remove_model_mark_remove_category_model_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partlist',
            name='mark',
            field=models.CharField(blank=True, max_length=250, verbose_name='Марка'),
        ),
    ]
