# Generated by Django 4.0.4 on 2022-04-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_mark_slug_partlist_list_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/shop'),
        ),
    ]
